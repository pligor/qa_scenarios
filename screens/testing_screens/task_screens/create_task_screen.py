from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss

new_task_summary_field = s(by.css("input#summary"))
new_task_summary_label = s(by.css("[for='summary']"))

new_task_description_field = s(by.css("textarea#description"))
new_task_description_label = s(by.css("[for='description']"))

new_task_submit_create_button = s(by.css("button[name='action']"))

new_task_status_field = s(by.css(".dropdown-trigger.select-dropdown"))
