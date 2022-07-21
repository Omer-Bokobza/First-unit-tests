import pytest
import homework_3
import logging

# add your specific path to filename to get the log text file
log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()


@pytest.fixture
def create_data_set():
    data_set = {100001: {"name": "Tal", "sex": "male", "age": 22},
                100002: {"sex": "female", "age": 57, "ID": 17686401, "name": "Anat"}, \
                100003: {"name": "Sharon", "age": 27, "sex": "female"},
                100004: {"name": "David", "age": 53, "sex": "male"}}
    return data_set


def test_split_male_female(create_data_set):
    '''
    testing the function split_male_female
    :param create_data_set: get a dict
    :return: Passed if its working
    '''
    log.info("test for split male and female function")
    print("")
    male_dict, female_dict = homework_3.split_male_female(create_data_set)
    assert len(male_dict) + len(female_dict) == len(create_data_set)


def test_find_median_average(create_data_set):
    log.info("test for find median average function")
    print("")
    assert "The median age is :", homework_3.find_median_average().median
    assert "The average age is :", homework_3.find_median_average().average


def test_print_values_above(create_data_set):
    """
    testing the function print_values_above
    :param create_data_set: get a dict
    :return: passed if its working
    """
    log.info("test for print values above function")
    print("")
    homework_3.print_values_above(create_data_set, 27)
