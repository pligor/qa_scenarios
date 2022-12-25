from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss
from helpers.random_helper import get_random_name, get_random_email

verify_title = s(by.css('.card-title'))
verify_content = s(by.css('.card-content p'))
