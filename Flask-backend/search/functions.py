
from api import db, Bid, Textbook, Auction
from sqlalchemy import func


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
    matchingIDs = []
    searchResults = []

    # search for keywords separately
    for keyword in keywords:
        queryResults.append(Textbook.query.filter(func.lower(Textbook.title).like("%" + keyword.lower() + "%")).all())

    # This was a regex that wasn't working
    # results.append(Textbook.query.filter(func.lower(Textbook.title).op('regexp')(r'\b{}\b'.format(keyword.lower()))).all())

    # If no textbook matches any of the keywords
    if len(queryResults) == 0:
        # Return an empty list
        return searchResults

    for result in queryResults:
        matchingIDs.append([r.id for r in result])


    # get all textbooks that contain every keyword
    for tID in matchingIDs[0]:
        allPresent = True
        for idList in matchingIDs[1:]:
            if tID not in idList:
                allPresent = False
                break
        if allPresent:
            searchResults.append(tID)

    print("IDs:", matchingIDs)
    return searchResults

