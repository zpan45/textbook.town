__author__ = 'piercesaly'

from api import db, Textbook
from sqlalchemy import func
from searchfunctions import countBids, search_by_title, search_by_course, userHasAlreadyBidOnTextbook


def main():
    print('Bids:', countBids(1))
    print(search_by_title("i%20like"))
    print(search_by_course("CS"))
    print(userHasAlreadyBidOnTextbook(2,2))


if __name__ == '__main__':
    main()



