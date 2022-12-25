from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss

create_project_button = s(by.css(".s12 >  .btn.waves-effect.waves-light"))

single_project_title = s(by.css(".card-title"))

single_project_description = s(by.css(".card-content > p"))

project_cards = ss(by.css(".card"))

single_project_edit_button = s(by.css("#btn_update_project"))

single_project_delete_button = s(by.css("#delete_project"))

single_project_add_task_button = s(by.css("#btn_add_task"))

single_project_view_tasks_button = s(by.css("#btn_view_tasks"))
