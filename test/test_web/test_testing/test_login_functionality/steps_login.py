from selene import Browser, be, have
from helpers.annotation_helpers import scenario_step
from helpers.pmtool_form_helpers import naturally_fill_pmtool_input
import pandas as pd
from screens.testing_screens.home_screen import login_menu_button, signup_menu_button
from screens.testing_screens.logged_in_main_menu import logout_menu_link, dashboard_menu_link, task_db_menu_link, settings_menu_link
from screens.testing_screens.login_screen import login_email_error, login_password_error, password_field, login_button, email_field, \
    login_label_email, login_label_password


@scenario_step
def step_logout():
    step_assert_we_are_logged_in()
    logout_menu_link.click()

@scenario_step
def step_assert_we_are_logged_in():
    logout_menu_link.should(have.exact_text('Logout'))
    dashboard_menu_link.should(have.exact_text('Dashboard'))
    task_db_menu_link.should(have.exact_text('TaskDB'))
    settings_menu_link.should(have.exact_text('Settings'))


@scenario_step
def step_access_dashboard_for_logged_in_user(mybrowser: Browser):
    step_assert_we_are_logged_in()

    mybrowser.open('/dashboard')


@scenario_step
def step_access_dashboard_for_logged_out_user(mybrowser: Browser):
    step_assert_we_are_logged_out()

    mybrowser.open('/dashboard')


@scenario_step
def step_assert_we_are_logged_out():
    login_menu_button.should(be.visible)
    signup_menu_button.should(be.visible)


@scenario_step
def step_assert_invalid_login(user: pd.Series):
    for elem in [login_email_error, login_password_error]:
        elem.should(be.visible)
        elem.should(have.exact_text('Invalid login info'))

    email_field.should(have.value(user.email))
    password_field.should(have.value(user.password))
    login_button.should(be.visible)


@scenario_step
def step_visit_login(mybrowser: Browser):
    login_menu_button.click()
    step_assert_login_is_reset(mybrowser)


@scenario_step
def step_assert_login_is_reset(mybrowser: Browser):
    mybrowser.should(have.url_containing('/login'))
    # neglect this warning from Pycharm, TODO report issue to Selene library

    email_field.should(have.value(''))
    password_field.should(have.value(''))
    login_button.should(be.visible)


@scenario_step
def step_login_user(user: pd.Series):
    naturally_fill_pmtool_input(label_elem=login_label_email, field_elem=email_field, characters=user.email)

    naturally_fill_pmtool_input(label_elem=login_label_password, field_elem=password_field, characters=user.password)

    login_button.click()
