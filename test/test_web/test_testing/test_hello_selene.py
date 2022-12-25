from selene import Browser

from logging import Logger
import pytest
from test.test_web.test_testing.test_login_functionality.steps_login import step_login_user, step_assert_we_are_logged_in
from time import sleep
from fixtures.chrome_fixtures import mybrowser
assert mybrowser is not None

# @pytest.mark.issue(issue_id="111111", reason="Some bug", issue_type="PB")
# @pytest.mark.hello_world
# def test_user():
#     user = Users['invalid']
#     print(user['password'])
#     # pytest.fail("we still need to implement this case")


@pytest.mark.hello_world
def test_hello_normal_speed(mybrowser: Browser, rp_logger: Logger, users: dict):
    secs = 3
    sleep(secs)
    mybrowser.open('/login')
    user = users['valid']
    sleep(secs)
    step_login_user(user=user)
    sleep(secs)
    step_assert_we_are_logged_in()
    sleep(secs)


@pytest.mark.hello_world
def test_hello_slow_speed(mybrowser: Browser, rp_logger: Logger, users: dict):
    secs = 5
    sleep(secs)
    mybrowser.open('/login')
    user = users['valid']
    sleep(secs)
    step_login_user(user=user)
    sleep(secs)
    step_assert_we_are_logged_in()
    sleep(secs)


@pytest.mark.hello_world
def test_hello_too_slow_speed(mybrowser: Browser, rp_logger: Logger, users: dict):
    secs = 10
    sleep(secs)
    mybrowser.open('/login')
    user = users['valid']
    sleep(secs)
    step_login_user(user=user)
    sleep(secs)
    step_assert_we_are_logged_in()
    sleep(secs)
