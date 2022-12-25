from selene import be
from helpers.annotation_helpers import scenario_step
from screens.testing_screens.logged_in_main_menu import dashboard_menu_link


@scenario_step
def step_visit_dashboard():
    dashboard_menu_link.should(be.visible).click()
