from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss

email_field = s(by.css("input#email"))
login_label_email = s(by.css("[for='email']"))

password_field = s(by.css("input#password"))
login_label_password = s(by.css("[for='password']"))

login_button = s(by.css("button[name='action']"))

login_email_error = s(by.css(".s12 .row:nth-of-type(1) .invalid-feedback"))

login_password_error = s(by.css(".row:nth-of-type(2) .invalid-feedback"))
