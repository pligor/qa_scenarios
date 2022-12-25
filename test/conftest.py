import pytest

from reportportal_client import RPLogger
import logging
from logging import Logger
from helpers.cmd_helper import freeze_requirements

def finalizer_function():
    print("This is executed after all scenarios have been executed and we are freezing the requirements in order to be sure that we can continue this to any virtual environment")
    freeze_requirements()


@pytest.fixture(scope="session", autouse=True)
def my_session_wrapper(request):
    # https://stackoverflow.com/questions/17801300/how-to-run-a-method-before-all-tests-in-all-classes
    print("prepare something ahead of all tests")
    request.addfinalizer(finalizer_function)


@pytest.fixture(scope="session")
def rp_logger() -> Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


# ############## THREE FUNCTIONS BELOW FOR CUSTOM MARKERS ###########################
# Inspired by https://docs.pytest.org/en/6.2.x/example/markers.html
# Use them as such: -C "C283, C456" -m 'testrail'
# it means you want to execute only those which have as at least one of their testrail parameters either the C283 or the C456
def pytest_addoption(parser):
    parser.addoption(
        "-C",
        action="store",
        metavar="TESTRAIL_IDS",
        help="only run tests matching the testrail TESTRAIL_IDS.",
    )


def pytest_runtest_setup(item):
    testcase_ids = [arg for mark in item.iter_markers(name="testrail")
                    for arg in mark.args]
    c_param = item.config.getoption("-C")
    if testcase_ids and c_param:
        options = [option.strip() for option in c_param.split(',')]
        if all([option not in testcase_ids for option in options]):
            pytest.skip(f"test requires testrail in {' or '.join(testcase_ids)} but you require {' or '.join(options)}")
