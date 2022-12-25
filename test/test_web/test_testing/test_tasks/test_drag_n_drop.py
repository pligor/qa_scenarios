from helpers.drag_n_drop_helpers import drag_n_drop_via_js
from screens.testing_screens.task_screens.tasks_screen import get_task_cards_by_name, in_review_container, \
    todo_container, in_progress_container
from test.test_web.test_testing.steps_main_menu import step_visit_dashboard
from test.test_web.test_testing.test_login_functionality.steps_login import step_login_user, step_assert_we_are_logged_in
from logging import Logger
from test.test_web.test_testing.test_tasks.steps_tasks import step_view_tasks_of_latest_project, step_assert_tasks_of_project_are_rendered, \
    step_assert_status_column_has_tasks
from selene import Browser, have
from fixtures.chrome_fixtures import mybrowser
assert mybrowser is not None

def test_drag_n_drop(mybrowser: Browser, rp_logger: Logger, users: dict):
    mybrowser.open('/login')

    user = users['two_tasks']

    step_login_user(user=user)

    step_assert_we_are_logged_in()

    rp_logger.info("Verify that dragging and dropping the task between columns should change its status")

    step_view_tasks_of_latest_project()

    step_assert_tasks_of_project_are_rendered(mybrowser)

    step_assert_status_column_has_tasks('todo', ['task_one'])
    step_assert_status_column_has_tasks('in progress', ['task_two'])

    cards = get_task_cards_by_name('task_one')
    cards.should(have.size(1))
    card_one = cards[0]

    drag_n_drop_via_js(from_elem=card_one, target_elem=in_review_container, driver=mybrowser.driver,
                       logger=rp_logger)

    step_assert_status_column_has_tasks('in progress', ['task_two'])
    step_assert_status_column_has_tasks('in review', ['task_one'])

    step_visit_dashboard()

    step_view_tasks_of_latest_project()

    step_assert_status_column_has_tasks('in progress', ['task_two'])
    step_assert_status_column_has_tasks('in review', ['task_one'])

    cards_two = get_task_cards_by_name('task_two')
    cards_two.should(have.size(1))
    card_two = cards_two[0]

    drag_n_drop_via_js(from_elem=card_two, target_elem=in_review_container, driver=mybrowser.driver,
                       logger=rp_logger)

    step_assert_status_column_has_tasks('in review', ['task_one', 'task_two'])

    drag_n_drop_via_js(from_elem=get_task_cards_by_name('task_one')[0],
                       target_elem=todo_container,
                       driver=mybrowser.driver, logger=rp_logger)

    drag_n_drop_via_js(from_elem=get_task_cards_by_name('task_two')[0],
                       target_elem=in_progress_container,
                       driver=mybrowser.driver, logger=rp_logger)

    step_assert_status_column_has_tasks('todo', ['task_one'])
    step_assert_status_column_has_tasks('in progress', ['task_two'])

    # from xpath: //span[text()='task_one']/parent::div/parent::div
    # to css: div#in_review_items
