#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from datetime import date

class Constants(object):
    """A class defining a fixed numer for some classes."""
    #
    # Exit statuses
    #
    EXIT_SUCCESS = 0
    EXIT_FAILURE = 1

    PROTOCOL = 'http://'
    STUDENT_ID_RE = re.compile('(g\d{7})')
    URL_RE = re.compile('http[s]?://((?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')

    KSU_TEMPLATE_INDEX = "ksu_index.html"

    # 'g'=bachelor or 'i'=master
    STUDENT_TYPE = 'g'

    # Probably, 4 is for computer science department.
    DEPARTMENT = 4 

    TODAY = date.today()

    @classmethod
    def get_grade(self, year):
        """Estimates a grade from an entrance year using a date.

        Example:
            if today -> 2016
            2016,2015,2014,2013 -> 1,2,3,4
        """
        if Constants.TODAY.month < 4:
            freshman_year = Constants.TODAY.year - 1
        else:
            freshman_year = Constants.TODAY.year
        return freshman_year - year + 1 

    @classmethod
    def get_year(self, grade):
        """Estimates a year from grade using a date.

        Example:
            if today -> 2016
            1,2,3,4 -> 2016,2015,2014,2013
        """
        if Constants.TODAY.month < 4:
            freshman_year = Constants.TODAY.year - 1
        else:
            freshman_year = Constants.TODAY.year
        return freshman_year - grade + 1 


def main():
    """Run an example for a Constants class."""
    print Constants.EXIT_SUCCESS
    print Constants.EXIT_FAILURE

    print Constants.PROTOCOL
    print Constants.STUDENT_ID_RE

    #2016,2015,2014,2013 -> 1,2,3,4
    print Constants.get_grade(2016)
    print Constants.get_grade(2015)
    print Constants.get_year(1)
    print Constants.get_year(2)
    assert Constants.get_year(Constants.get_grade(2016)) == 2016
    assert Constants.get_year(Constants.get_grade(2015)) == 2015
    assert Constants.get_year(Constants.get_grade(2014)) == 2014
    assert Constants.get_year(Constants.get_grade(2013)) == 2013
    assert Constants.get_year(Constants.get_grade(2012)) == 2012
    assert Constants.get_year(Constants.get_grade(2011)) == 2011
    assert Constants.get_year(Constants.get_grade(2010)) == 2010
    assert Constants.get_year(Constants.get_grade(2009)) == 2009

    return Constants.EXIT_SUCCESS

if __name__ == '__main__':
    sys.exit(main())
