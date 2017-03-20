__author__ = 'piercesaly'

from api import db, Textbook
from sqlalchemy import func
from search.functions import countBids, search_by_title, search_by_course, checkAndModifyAuctionIsCurrent


def main():
    print('Bids:', countBids(1))
    print(search_by_title("i%20like"))
    print(search_by_course("CS"))



if __name__ == '__main__':
    main()



