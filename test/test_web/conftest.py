import pytest
from reportportal_client import RPLogger
from os import environ

msec_BETWEEN_KEYBOARD_KEYS = 50
IMPLICIT_WAIT = 5
ENVIRONMENT_VAR_HEADLESS = "HEADLESS"


@pytest.fixture(scope="session")
def implicit_wait() -> int:
    # https://stackoverflow.com/questions/17801300/how-to-run-a-method-before-all-tests-in-all-classes
    return IMPLICIT_WAIT


@pytest.fixture(scope='session')
def is_headless() -> bool:
    headless = environ.get(ENVIRONMENT_VAR_HEADLESS)
    if headless is not None:
        is_headless = headless.lower()
        if not (is_headless == 'false' or is_headless == 'true'):
            raise Exception('headless environment variable can either be "true" or "false"')

    return eval(headless.lower().capitalize()) \
        if ENVIRONMENT_VAR_HEADLESS in environ.keys() else False
