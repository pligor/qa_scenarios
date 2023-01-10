from selene import Browser, have, be

from helpers.annotation_helpers import scenario_step
from helpers.pmtool_form_helpers import naturally_fill_pmtool_input
from helpers.selene_helpers import safe_clear_input_element
from screens.testing_screens.home_screen import signup_menu_button

from screens.testing_screens.signup_screen import SignupForm, name_field, email_field, password_field, company_field, address_field, \
    signup_action, label_name, label_email, label_password, label_company, label_address, name_error_message, \
    email_error_message, password_error_message, does_name_error_exists, does_password_error_exists
from screens.testing_screens.verify_account_screen import verify_title, verify_content


@scenario_step
def step_register_new_user(mybrowser: Browser, signup_form: SignupForm):
    # mybrowser.open('/signup')
    step_visit_signup(mybrowser)
    step_fill_signup_form(signup_form=signup_form)
    step_assert_signup_form(signup_form=signup_form)
    step_submit_signup()
    step_assert_verify_screen()


@scenario_step
def step_assert_signup_form(signup_form: SignupForm):
    name_field.should(have.value(signup_form.name))
    email_field.should(have.value(signup_form.email))
    password_field.should(have.value(signup_form.password))
    company_field.should(have.value(signup_form.company))
    address_field.should(have.value(signup_form.address))
    signup_action.should(be.clickable)


@scenario_step
def step_assert_verify_screen():
    verify_title.should(be.visible.and_(have.exact_text('Verify your account')))
    verify_content.should(be.visible)


@scenario_step
def step_visit_signup(mybrowser: Browser):
    mybrowser.open('/')
    signup_menu_button.click()


@scenario_step
def step_assert_empty_signup_form():
    name_field.should(have.value(''))
    email_field.should(have.value(''))
    password_field.should(have.value(''))
    company_field.should(have.value(''))
    address_field.should(have.value(''))


@scenario_step
def step_submit_signup():
    # In a solid system any of these four ways below should work
    # company_field.send_keys(Keys.ENTER)
    # address_field.send_keys(Keys.RETURN)
    # address_field.submit()
    signup_action.click()


@scenario_step
def step_clear_signup_form():
    for elem in [name_field, email_field, password_field, company_field, address_field]:
        safe_clear_input_element(elem)


@scenario_step
def step_fill_signup_form(signup_form: SignupForm):
    # TODO (low prio)
    # check why send_keys is not working as expected and prefixes with previous send keys IF set_value is used for clear

    naturally_fill_pmtool_input(label_elem=label_name, field_elem=name_field, characters=signup_form.name)

    naturally_fill_pmtool_input(label_elem=label_email, field_elem=email_field, characters=signup_form.email)

    naturally_fill_pmtool_input(label_elem=label_password, field_elem=password_field, characters=signup_form.password)

    naturally_fill_pmtool_input(label_elem=label_company, field_elem=company_field, characters=signup_form.company)

    naturally_fill_pmtool_input(label_elem=label_address, field_elem=address_field, characters=signup_form.address)


@scenario_step
def step_assert_invalid_error_messages_for_required_fields():
    for elem in [name_error_message, email_error_message, password_error_message]:
        elem.should(be.existing).should(have.text("This field is required"))


@scenario_step
def step_assert_only_invalid_error_message_for_wrong_email():
    if does_name_error_exists():
        name_error_message.should(have.exact_text(''))

    if does_password_error_exists():
        password_error_message.should(have.exact_text(''))

    email_error_message.should(have.text("Invalid email format"))
