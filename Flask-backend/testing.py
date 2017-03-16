__author__ = 'piercesaly'

from api import db, Textbook
from sqlalchemy import func
from search.functions import countBids, search_by_title


def main():
    print('Bids:', countBids(7))
    print(search_by_title("golf"))



if __name__ == '__main__':
    main()



