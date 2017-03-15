__author__ = 'piercesaly'

from api import db, Textbook
from sqlalchemy import func
from search.functions import countBids, search_by_title


def main():
    print('Bids:', countBids(1))
    print(search_by_title("i%20hate%20grails"))



if __name__ == '__main__':
    main()



