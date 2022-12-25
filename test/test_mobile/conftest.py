from os import environ
from subprocess import Popen

from helpers.cmd_helper import start_appium, kill_appium

OS_ENV_VAR_NAME = "OS"

def get_current_os():
    os_env_var = environ.get(OS_ENV_VAR_NAME)
    assert os_env_var is not None, "please specify an environment variable in front of pytest, e.g. OS=iOS pytest ..."
    return os_env_var.lower()

if get_current_os() == 'android':
    from test.test_mobile.fixtures.android_fixtures import *
elif get_current_os() == 'ios':
    from test.test_mobile.fixtures.ios_fixtures import *
else:
    raise Exception(f'Something is wrong with the implementation as we have a non expected Operating System: "{get_current_os()}"')

import pytest

IMPLICIT_WAIT = 10

@pytest.fixture(scope="session")
def implicit_wait() -> int:
    # https://stackoverflow.com/questions/17801300/how-to-run-a-method-before-all-tests-in-all-classes
    return IMPLICIT_WAIT

# @pytest.fixture(scope='session', autouse=True)
# def appium_process(rp_logger: Logger):
#     proc = start_appium()
#     rp_logger.info('Started appium')
#     yield
#     kill_appium(proc)
#     rp_logger.info('Killed appium')


@pytest.fixture(scope='session')
def appium_process(rp_logger: Logger) -> Popen:
    proc = start_appium()
    rp_logger.info('Started appium')
    return proc

@pytest.fixture(scope='session', autouse=True)
def appium_terminator(rp_logger: Logger, appium_process: Popen):
    yield
    kill_appium(appium_process)
    rp_logger.info('Killed appium')

@pytest.fixture(autouse=True, scope='function')
def terminator(driver: webdriver.Remote, app_id, rp_logger: Logger):
    yield  # execute the function first
    rp_logger.info("terminating app")
    try:
        terminated = driver.terminate_app(app_id=app_id)
        assert terminated, "app is expected to be terminated successfully upon finish of one scenario"
    finally:
        driver.quit()
