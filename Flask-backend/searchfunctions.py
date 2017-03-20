__author__ = 'piercesaly'

from api import db, Bid, Textbook, Auction
from sqlalchemy import func
from validate import getCurrentESTDate


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
    # tokenize keywords
    keywords = searchString.split('%20')

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
    # tokenize keywords
    keywords = searchString.split('%20')

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


def checkAndModifyAuctionIsCurrent(textbookID):
    '''
    Checks if the auction has closed, and updates isCurrent auction property accordingly
    :param textbookID: ID of textbook
    :return:
    '''
    bookAuction = Auction.query.get(textbookID)
    if getCurrentESTDate() > bookAuction.closingDate:
        bookAuction.isCurrent = False
        db.session.commit()


def currentUserHasAlreadyBidOnTextbook(user, textbookID):
    pass


def collectTextbookSearchResultInfo(textbookID):
    pass