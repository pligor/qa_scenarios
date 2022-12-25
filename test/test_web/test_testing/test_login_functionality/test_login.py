from logging import Logger
import pytest
from selene.support.shared import browser
from fixtures.chrome_fixtures import mybrowser
from screens.testing_screens.signup_screen import SignupForm
from test.test_web.test_testing.test_dashboard_functionality.steps_dashboard import step_assert_dashboard_screen_is_rendered
from test.test_web.test_testing.test_login_functionality.steps_login import step_login_user, step_assert_we_are_logged_in, \
    step_access_dashboard_for_logged_in_user, step_logout, step_access_dashboard_for_logged_out_user, \
    step_assert_login_is_reset, step_visit_login, step_assert_invalid_login
from test.test_web.test_testing.test_signup_functionality.steps_signup import step_register_new_user

assert mybrowser is not None


def test_valid_login(mybrowser: browser, rp_logger: Logger, users: dict):
    rp_logger.info('Verify that using valid credentials in the Login screen will yield the dashboard screen of the app')

    mybrowser.open('/login')

    user = users['valid']

    step_login_user(user=user)

    step_assert_we_are_logged_in()

    step_assert_dashboard_screen_is_rendered(mybrowser)

    rp_logger.info('Verify that if a user is already logged in and attempts to navigate to the dashboard screen, '
                   'then the user will be allowed to have access to the dashboard screen, namely that the login state'
                   ' is preserved')

    step_access_dashboard_for_logged_in_user(mybrowser)

    step_assert_dashboard_screen_is_rendered(mybrowser)

    rp_logger.info('Verify that logging out of the Dashboard and attempting to access the Dashboard screen will '
                   'redirect the user back to the login screen')

    step_logout()

    step_access_dashboard_for_logged_out_user(mybrowser)

    step_assert_login_is_reset(mybrowser)


@pytest.mark.disabled
@pytest.mark.smoke
def test_login_scenario(mybrowser: browser, rp_logger: Logger, users: dict):
    """
    Verify that attempting to login with an invalid user will throw an error message and not be authorized to user the system
    """

    signup_form = SignupForm.random()
    step_register_new_user(mybrowser, signup_form=signup_form)

    step_visit_login(mybrowser)

    rp_logger.info('Verify that using invalid credentials in the Login screen will yield an error message and keep '
                   'user in the login page')

    user = users['invalid']

    step_login_user(user=user)

    step_assert_invalid_login(user=user)

    del user

    rp_logger.info('Verify that after using invalid credentials in the Login screen and the error message is '
                   'received, when the user changes the input values of either the email or the password, the invalid '
                   'login info error message should vanish and the Login button should become enabled once again')

    step_access_dashboard_for_logged_out_user(mybrowser)

    step_assert_login_is_reset(mybrowser)

    rp_logger.info('Verify that using valid credentials in the Login screen will yield the dashboard screen of the app')

    user = signup_form.to_pandas_series()
    rp_logger.info('USER: %s' % user)

    step_login_user(user=user)

    # TODO high priority
    pytest.fail('''
    Here we declare it as failure since we already spent a large enough amount of time and effort to try and understand
    why the user is not properly registered and therefore cannot login while if we attempt to do it manually this will
    always succeed.
    We tried with the help of a Proxy to observe the requests between manual execution and automated and they are
    identical.
    We have updated all libraries to the latest ones.
    This could have been an issue of the chose library Selene but there is no time to deviate from now.
    Another attempt that we did was to try and submit the form with all the various ways there are but still no luck.
    Finally we introduced sleep executions between steps in order to make the execution in a more natural speed, but
    this did not help either.
    We even tried to click on input elements before entering values as the user would normally do but no luck once more.
    
    Next idea was to prevent Chrome from understanding us as being an automation script, this is an ongoing process.
    A parallel idea would be to try the entire script in another operating system as we are currently in MacOS, perhaps
    in a Linux could work better.
    For the purposes of this exercise we will be working with fixed pre-created users
    ''')

    step_assert_we_are_logged_in()

    step_assert_dashboard_screen_is_rendered(mybrowser)

    # TODO more steps to be automated
