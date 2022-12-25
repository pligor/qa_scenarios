from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss

new_project_name_field = s(by.css("input#name"))
new_project_name_label = s(by.css("[for='name']"))

new_project_description_field = s(by.css("input#description"))
new_project_description_label = s(by.css("[for='description']"))

new_project_submit_create_button = s(by.css("button[name='action']"))
