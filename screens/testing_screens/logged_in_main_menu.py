from selene import by, be, have, query
from selene.support.shared.jquery_style import s, ss

logout_menu_link = s(by.css("a#logout"))

dashboard_menu_link = s(by.css("a#dashboard"))

task_db_menu_link = s(by.css("a#task_db"))

settings_menu_link = s(by.css("a#settings"))
