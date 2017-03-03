__author__ = 'piercesaly'

import datetime

def validPubYear(year):
    '''
    Determines whether or not a year string is valid (Between 0 and 2017)
    :param year: year in string format
    :return: True if valid, False otherwise
    '''
    try:
        y = int(year)
    except ValueError:
        return False

    if y > 0 and y < 2018:
        return True


def validDateString(str):
    try:
        stringToDate(str)
    except ValueError:
        return False
    return True


def stringToDate(str):
    return datetime.datetime.strptime(str, '%Y-%m-%d').date()

