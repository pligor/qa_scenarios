from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss

edit_project_name_field = s(by.css("input#name"))
edit_project_name_label = s(by.css("[for='name']"))

edit_project_description_field = s(by.css("input#description"))
edit_project_description_label = s(by.css("[for='description']"))

edit_project_submit_update_button = s(by.css("button[name='action']"))
