__author__ = 'piercesaly'

import datetime

UTC_TIME_ADJUSTMENT = 4             # will have to change when daylight savings kicks in

def validPubYear(year):
    '''
    Determines whether or not a year string is valid and between 1900 and 2017
    :param year: year in string format
    :return: True if valid, False otherwise
    '''
    try:
        y = int(year)
    except ValueError:
        return False

    if 1899 < y < 2018:
        return True
    else:
        return False


def getCurrentESTDate():
    '''
    :return: current date in EST (depends on the UTC_TIME_ADJUSTMENT being correct for daylight savings time)
    '''
    d = datetime.datetime.utcnow() - datetime.timedelta(hours=UTC_TIME_ADJUSTMENT)
    return d.date()


def validDateString(string):
    '''
    Date must be a valid date string and must be between tomorrow and 60 days
    :param string:
    :return:
    '''
    try:
        d = stringToDate(string)
    except ValueError:
        return False

    return getCurrentESTDate() < d < getCurrentESTDate() + datetime.timedelta(days=60)


def stringToDate(string):
    '''
    Converts dateString 'yyyy-mm-dd' to a date object
    :param string: string to convert to date
    :return: date object
    '''
    return datetime.datetime.strptime(string, '%Y-%m-%d').date()

def dateToString(dateObj):
    '''
    Converts dateString 'yyyy-mm-dd' to a date object
    :param string: string to convert to date
    :return: date object
    '''

    return dateObj.strftime("%b %d, %Y").replace(" 0", " ")


def validBid(bid):
    '''
    Minimum bid must be a positive integer
    :param bid: minimumBid as a string
    :return: True or False
    '''
    try:
        b = int(bid)
    except ValueError:
        return False

    return b > 0

