__author__ = 'piercesaly'

from api import db, Textbook
from sqlalchemy import func
from search.functions import countBids



def main():
    print('Bids:', countBids(1))


def queryPractice(string):
    results = Textbook.query.filter(func.lower(Textbook.title).like("%" + string.lower() + "%")).all()
    for r in results:
        print(r.id)




if __name__ == '__main__':
    main()



