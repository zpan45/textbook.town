
from api import db, Bid

def countBids(auctionID):
    '''
    Count bids for auction
    :param auctionID: id of auction
    :return: number of bids in this auction
    '''

    bids = Bid.query.filter_by(auction=auctionID).all()
    return len(bids)

