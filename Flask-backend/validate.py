__author__ = 'piercesaly'

import datetime

UTC_TIME_ADJUSTMENT = 5             # will have to change when daylight savings kicks in

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

    if 1899 < y < 2018:
        return True
    else:
        return False


def getCurrentESTDate():
    d = datetime.datetime.utcnow() - datetime.timedelta(hours=UTC_TIME_ADJUSTMENT)
    return d.date()


def validDateString(str):
    '''
    Date must be a valid date string and must be tomorrow or later
    :param str:
    :return:
    '''
    try:
        d = stringToDate(str)
    except ValueError:
        return False

    if d <= getCurrentESTDate():
        return False

    return True


def stringToDate(str):
    return datetime.datetime.strptime(str, '%Y-%m-%d').date()

