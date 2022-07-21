import pytest
from homework_4 import Date
import logging

# add your specific path to filename to get the log text file
log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()


@pytest.fixture()
def new_date():
    date = Date(25, 7, 2003)
    return date



def test_is_valid(new_date):
    log.info("test for is_valid function")
    assert new_date
    log.debug("the date is valid")


def test_getNextDay(new_date):
    log.info("test for getNextDay function")
    next_day = Date(26, 7, 2003)
    assert new_date.getNextDay() == next_day
    log.DEBUG = f"the next day of {new_date} is {next_day}"


def test_getNextDays(new_date):
    log.info("test for getNextDays function")
    date_after_add = Date(1, 11,2003)
    assert new_date.getNextDays(98) == date_after_add
    log.DEBUG = f"the date was {new_date} and now its {date_after_add} after days add"


def test_eq(new_date):
    log.info("test for equals function")
    eq_date = Date(25, 7, 2003)
    assert new_date == eq_date
    log.DEBUG = f"{new_date} equals to {eq_date}"


def test_gt(new_date):
    log.info("test for greater than function")
    gt_date = Date(2, 3, 1990)
    assert new_date > gt_date
    log.DEBUG = f"{new_date} greater than {gt_date}"



def test_lt(new_date):
    log.info("test for lower than function")
    lt_date = Date(13, 4, 2010)
    assert new_date < lt_date
    log.DEBUG = f"{new_date} lower than {lt_date}"



def test_sub(new_date):
    log.info("test for sub function")
    sub_date = Date(2, 12, 1998)
    assert new_date - sub_date
    log.DEBUG = f"the day difference  between {new_date} and {sub_date}"
