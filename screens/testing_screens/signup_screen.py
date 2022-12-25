from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss
from helpers.random_helper import get_random_name, get_random_email, get_random_numbers
import pandas as pd

name_field_selector = by.css("input#fullName")
name_field = s(name_field_selector)
label_name = s(by.css("[for='fullName']"))

email_field_selector = by.css("input#email")
email_field = s(email_field_selector)
label_email = s(by.css("[for='email']"))

password_field_selector = by.css("input#password")
password_field = s(password_field_selector)
label_password = s(by.css("[for='password']"))

company_field_selector = by.css("input#company")
company_field = s(company_field_selector)
label_company = s(by.css("[for='company']"))

address_field_selector = by.css("input#address")
address_field = s(address_field_selector)
label_address = s(by.css("[for='address']"))

signup_action_selector = by.css("button[name='action']")
signup_action = s(signup_action_selector)

name_error_message_selector = by.css(".s12 .row:nth-of-type(1) .invalid-feedback")
name_error_message = s(name_error_message_selector)

email_error_message_selector = by.css(".row:nth-of-type(2) .invalid-feedback")
email_error_message = s(email_error_message_selector)

password_error_message_selector = by.css(".row:nth-of-type(3) .invalid-feedback")
password_error_message = s(password_error_message_selector)


def does_name_error_exists():
    return len(ss(name_error_message_selector)) > 0


def does_password_error_exists():
    return len(ss(password_error_message_selector)) > 0


def confirm_we_are_in_signup_screen() -> None:
    for elem in [name_field, email_field, password_field, company_field, address_field, signup_action]:
        elem.should(be.visible)


class SignupForm(object):

    def __init__(self, name, email, password, company=None, address=None) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.password = password
        self.company = company
        self.address = address

    @staticmethod
    def random():
        return SignupForm(name=f'{get_random_name(5)}Dela{get_random_name(8)}',
                          email=get_random_email(prefix='pligor.george+', domain='gmail.com'),
                          password=f'{get_random_name(6)}{get_random_numbers(2)}',
                          company=get_random_name(5),
                          address=get_random_name(5))

    def set_invalid_email(self, invalid_email='email.com'):
        self.email = invalid_email
        return self

    def to_pandas_series(self):
        return pd.Series([self.name, self.email, self.password, self.company, self.address],
                         index=['fullname', 'email', 'password', 'company', 'address'])
