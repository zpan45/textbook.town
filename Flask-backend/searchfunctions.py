__author__ = 'piercesaly'

from api import db, Bid, Textbook, Auction, User, SERVER
from flask import jsonify
from sqlalchemy import func
from validate import getCurrentESTDate, dateToString


def countBids(auctionID):
    '''
    Count bids for auction
    :param auctionID: id of auction
    :return: number of bids in this auction
    '''

    bids = Bid.query.filter_by(auction=auctionID).all()
    return len(bids)


def search_by_title(searchString):
    '''
    Searches database for textbooks by title
    :param searchString: query entered by the user (separated by %20 instead of spaces)
    :return: List of textbook ids that match search criteria
    '''
    # tokenize keywords (split at spaces because flask converts %20 to spaces automatically)
    keywords = searchString.split()

    queryResults = []


    # search for keywords separately
    for keyword in keywords:
        queryResults.append(Textbook.query.filter(func.lower(Textbook.title).like("%" + keyword.lower() + "%")).all())

    # This was a regex that wasn't working
    # results.append(Textbook.query.filter(func.lower(Textbook.title).op('regexp')(r'\b{}\b'.format(keyword.lower()))).all())

    return _filter_query_results(queryResults)


def search_by_course(searchString):
    '''
    Searches database for textbooks by course.
    For best matching, query with a space between subject and course code
    :param searchString: query entered by the user (separated by %20 instead of spaces)
    :return: List of textbook ids that match search criteria
    '''
    # tokenize keywords (split at spaces because flask converts %20 to spaces automatically)
    keywords = searchString.split()

    queryResults = []

    # search for keywords separately
    for keyword in keywords:
        queryResults.append(Textbook.query.filter(func.lower(Textbook.course).like("%" + keyword.lower() + "%")).all())

    return _filter_query_results(queryResults)


def _filter_query_results(queryResults):
    '''
    Helper method to filter down results to only books that contain all keywords in search
    :param queryResults: 2d list of all book IDs matching each search keyword
    :return: list of filtered textbook IDs
    '''
    matchingIDs = []
    searchResults = []

    # If no textbook matches any of the keywords
    if len(queryResults) == 0:
        # Return an empty list
        return searchResults

    for result in queryResults:
        matchingIDs.append([r.id for r in result])

    # get all textbooks that contain every keyword
    for tID in matchingIDs[0]:
        # Check if auctions have closed
        allPresent = True
        for idList in matchingIDs[1:]:
            if tID not in idList:
                allPresent = False
                break
        if allPresent:
            searchResults.append(tID)

    # filter search results to only include textbooks currently on auction
    # return [tID for tID in searchResults if Auction.query.get(tID).isCurrent]

    return searchResults


def search_by_next_closing():
    '''
    Get list of current textbooks sorted by soonest closing date first
    :return: List of textbook IDs sorted by closing Date
    '''
    updateIsCurrentForAllAuctions()
    currentAuctions = Auction.query.filter_by(isCurrent=True).all()
    currentAuctions.sort(key=lambda auc: auc.closingDate)
    # dates = [a.closingDate for a in currentAuctions]
    # print(dates)

    # get corresponding textbookIDs
    return [auction.textbook for auction in currentAuctions]

def updateIsCurrentForAllAuctions():
    '''
    Updates the isCurrent property for all auctions in the database
    :return: None
    '''
    for auction in Auction.query.filter_by(isCurrent=True).all():
        if auction.closingDate < getCurrentESTDate():
            auction.isCurrent = False

    db.session.commit()


def updateIsCurrent(textbookID):
    '''
    Checks if the auction has closed, and updates isCurrent auction property accordingly
    :param textbookID: ID of textbook
    :return:
    '''
    bookAuction = Auction.query.get(textbookID)
    if bookAuction is None:
        return
    if getCurrentESTDate() > bookAuction.closingDate:
        bookAuction.isCurrent = False
        db.session.commit()


def userHasAlreadyBidOnTextbook(userID, textbookID):
    '''
    Returns whether or not specified user has already bid on specified textbook
    :param userID: id of user
    :param textbookID: id of textbook
    :return:
    '''
    auction = Auction.query.filter_by(textbook=textbookID).first()
    if auction is None:
        print("WOAH THAT AUCTION DOESN'T EXIST")
        return False
    previousBid = Bid.query.filter_by(auction=auction.id, bidder=userID).first()

    return True if previousBid is not None else False


def userIsBuyerOfTextbook(userID, textbookID):
    '''
    Returns whether or not specified user is the buyer of the specified textbook
    :param userID: id of user
    :param textbookID: id of textbook
    :return: true if user is buyer, false if user is seller
    '''
    book = Textbook.query.get(textbookID)

    if book is None:
        return False

    return userID != book.seller


def collectTextbookSearchResultInfo(textbookID):
    '''
    Returns a dictionary with the proper textbook info for search result JSON
    :param textbookID: id of textbook
    :return: dictionary
    '''
    data = {}

    textbook = Textbook.query.get(textbookID)

    data['id'] = textbookID
    data['title'] = textbook.title
    data['author'] = textbook.author
    data['subject'] = textbook.course
    data['image'] = SERVER + "img/" + textbook.coverPhotoName

    auction = Auction.query.filter_by(textbook=textbookID).first()
    data['date_closing'] = dateToString(auction.closingDate)
    data['tag'] = 'Last Day' if getCurrentESTDate() == auction.closingDate else ''
    data['bids'] = countBids(auction.id)
    data['price'] = auction.minimumBid

    return data


def determineTop3BidsAfterClose(textbookID):
    '''
    Returns 3-element list of the top 3 bids on an auction
    :param textbookID: ID of textbook
    :return: 3 element list containing top 3 bids
    '''

    # winning bidder pays second bidder ceiling + this amount (or their ceiling, whatever's lower)
    WINNING_INCREMENT = 5

    # get corresponding auction ID
    auction = Auction.query.filter_by(textbook=textbookID).first()
    if auction is None:
        return []

    auctionID = auction.id

    # get all bids on the auction and sort by bid ceiling
    allBids = Bid.query.filter_by(auction=auctionID).all()
    allBids.sort(key=lambda bid: bid.ceiling, reverse=True)

    if len(allBids) < 2:
        return allBids

    secondBidPlusIncrement = allBids[1].ceiling + WINNING_INCREMENT
    if (secondBidPlusIncrement < allBids[0].ceiling):
        allBids[0].ceiling = secondBidPlusIncrement

    # bids = [b.ceiling for b in allBids]
    # print(bids)

    if len(allBids) <= 3:
        return allBids
    else:
        return allBids[:3]


def jsonifyBuyerViewResponse(textbookID):
    book = Textbook.query.get(textbookID)

    if book is None:
        return jsonify({'status': 'failure', 'message': 'that textbook does not exist'})

    res = book.as_dict()

    del res['coverPhotoName']
    del res['bestPhotoName']
    del res['worstPhotoName']
    del res['averagePhotoName']

    res['coverPhoto'] = SERVER + "img/" + book.coverPhotoName
    res['bestPhoto'] = SERVER + "img/" + book.bestPhotoName
    res['worstPhoto'] = SERVER + "img/" + book.worstPhotoName
    res['averagePhoto'] = SERVER + "img/" + book.averagePhotoName

    res['status'] = 'success'

    correspondingAuction = Auction.query.get(book.auction)
    res['closingDate'] = dateToString(correspondingAuction.closingDate)
    res['minimumBid'] = correspondingAuction.minimumBid
    res['isCurrent'] = correspondingAuction.isCurrent

    return jsonify(res)


def jsonifySellerViewResponse(textbookID):
    book = Textbook.query.get(textbookID)

    if book is None:
        return jsonify({'status': 'failure', 'message': 'that textbook does not exist'})

    res = book.as_dict()

    del res['coverPhotoName']
    del res['bestPhotoName']
    del res['worstPhotoName']
    del res['averagePhotoName']

    res['coverPhoto'] = SERVER + "img/" + book.coverPhotoName
    res['bestPhoto'] = SERVER + "img/" + book.bestPhotoName
    res['worstPhoto'] = SERVER + "img/" + book.worstPhotoName
    res['averagePhoto'] = SERVER + "img/" + book.averagePhotoName

    res['status'] = 'success'

    correspondingAuction = Auction.query.get(book.auction)
    res['closingDate'] = dateToString(correspondingAuction.closingDate)
    res['minimumBid'] = correspondingAuction.minimumBid
    res['isCurrent'] = correspondingAuction.isCurrent

    if not correspondingAuction.isCurrent:

        top3 = determineTop3BidsAfterClose(textbookID)

        topBids = []
        for bid in top3:
            user = User.query.get(bid.bidder)
            topBids.append({'bid': bid.ceiling, 'user_name': user.username, 'profile_link': user.contact})

        res['bids'] = topBids

    return jsonify(res)


def deleteBook(textbookID):
    book = Textbook.query.get(textbookID)

    if book is None:
        return jsonify({'status': 'failure', 'message': 'that textbook does not exist'})

    auction = Auction.query.get(book.auction)

    if auction is None:
        return jsonify({'status': 'failure', 'message': 'that textbook does not exist'})

    db.session.delete(book)
    db.session.delete(auction)
    db.session.commit()

    return jsonify({'status': 'success'})
