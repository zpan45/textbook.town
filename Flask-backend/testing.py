__author__ = 'piercesaly'

from api import db, Textbook
from sqlalchemy import func
from search.functions import countBids, search_by_title


def main():
    print('Bids:', countBids(1))
    print(search_by_title("liKE%20I%20o"))


def queryPractice(string):
    '''
    Foundation of the search_by_title method in search/functions.py
    :param string: search string
    :return:
    '''
    keywords = string.split()
    results = []
    matchingIDs = []

    for keyword in keywords:
        results.append(Textbook.query.filter(func.lower(Textbook.title).like("%" + keyword.lower() + "%")).all())

    # results.append(Textbook.query.filter(func.lower(Textbook.title).op('regexp')(r'\b{}\b'.format(keyword.lower()))).all())

    # If no textbook matches any of the keywords
    if len(results) == 0:
        # Return an empty list or something like that
        pass

    for result in results:
        matchingIDs.append([r.id for r in result])

    allPresent = True

    searchResults = []

    for id in matchingIDs[0]:
        for idList in matchingIDs[1:]:
            if id not in idList:
                allPresent = False
                break
        if allPresent:
            searchResults.append(id)

    print(searchResults)




if __name__ == '__main__':
    main()



