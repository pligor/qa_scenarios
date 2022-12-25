from selene import Browser
from screens.testing_screens.signup_screen import confirm_we_are_in_signup_screen, SignupForm
from test.test_web.test_testing.test_signup_functionality.steps_signup import step_visit_signup, step_assert_empty_signup_form, \
    step_submit_signup, step_assert_invalid_error_messages_for_required_fields, step_fill_signup_form, \
    step_assert_only_invalid_error_message_for_wrong_email, step_clear_signup_form, step_assert_verify_screen
from logging import Logger
from fixtures.chrome_fixtures import mybrowser
assert mybrowser is not None


def test_full_signup(mybrowser: Browser, rp_logger: Logger):
    step_visit_signup(mybrowser)

    rp_logger.info("Verify that submitting the Signup form when no inputs but filled the Optional fields will yield "
                   "error messages to the rest of the fields and the user will remain in Signup screen but leave "
                   "intact the Optional fields")
    step_assert_empty_signup_form()

    step_submit_signup()

    step_assert_invalid_error_messages_for_required_fields()

    confirm_we_are_in_signup_screen()

    rp_logger.info("Verify that filling all the fields with valid values plus the Company optional field but using a "
                   "wrong email will yield an error message regarding the format of the email")

    signup_form_with_invalid_email = SignupForm.random().set_invalid_email()

    step_fill_signup_form(signup_form=signup_form_with_invalid_email)

    # just to clear the memory and be sure that this is not used later
    del signup_form_with_invalid_email

    step_submit_signup()

    step_assert_only_invalid_error_message_for_wrong_email()

    rp_logger.info("Verify that filling only the required fields with valid inputs and clicking on Signup multiple "
                   "times will yield only one signup to the specified email address and the Verify your account page "
                   "will be rendered")

    step_clear_signup_form()

    signup_form = SignupForm.random()

    step_fill_signup_form(signup_form=signup_form)

    step_submit_signup()

    step_assert_verify_screen()
