from typing import Final
from selene import Browser

from helpers.alert_helpers import dismiss_alert, accept_alert
from screens.testing_screens.task_screens import BasicTask
from test.test_web.test_testing.test_login_functionality.steps_login import step_login_user, step_assert_we_are_logged_in, \
    step_access_dashboard_for_logged_in_user
from test.test_web.test_testing.test_projects.steps_project import step_fill_project_form, step_visit_create_new_project, \
    step_assert_create_project_screen_is_empty, step_submit_new_project_form, step_assert_single_project_in_dashboard, \
    step_create_new_project_from_dashboard, step_assert_two_projects, step_visit_edit_screen_of_project, \
    step_assert_edit_screen_of_project, step_edit_project_name, step_edit_project_description, step_delete_project, \
    step_delete_all_projects
from test.test_web.test_testing.test_tasks.steps_tasks import step_visit_add_task_of_project, step_assert_empty_add_task_form, \
    step_add_task, step_assert_tasks_of_project_are_rendered, step_assert_single_basic_task, \
    step_view_tasks_of_latest_project, step_assert_project_tasks_are_empty
from logging import Logger
from screens.testing_screens.project_screens import Project
from fixtures.chrome_fixtures import mybrowser
assert mybrowser is not None


def test_project_fully(mybrowser: Browser, rp_logger: Logger, users: dict):
    mybrowser.open('/login')

    user = users['projects']

    step_login_user(user=user)

    step_assert_we_are_logged_in()

    rp_logger.info('Verify that providing valid inputs will allow the user to create a Project and the new project '
                   'will be added in the Dashboard with the exactly the same attributes that the user used to create '
                   'it and this is true for any new Project that is created')

    first_project: Final = Project('first project', 'this is our 1st proj')
    second_project: Final = Project('Second', 'project')

    ###vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    step_visit_create_new_project()

    step_assert_create_project_screen_is_empty()

    step_fill_project_form(project=first_project)

    step_submit_new_project_form()

    step_assert_single_project_in_dashboard(project=first_project)

    step_create_new_project_from_dashboard(mybrowser, second_project)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    step_assert_two_projects(first_project, second_project, rp_logger)

    rp_logger.info('Verify that editing a Project and changing only its name will alter the Project’s name and keep '
                   'the description intact and vice versa, and this will be depicted in the Dashboard')

    projs = [first_project, second_project]
    index: Final = 0
    another_index = (index + 1) % 2

    proj = projs[index]
    another_proj = projs[another_index]
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    step_visit_edit_screen_of_project(index=index)

    step_assert_edit_screen_of_project(proj)

    proj = proj._replace(name='altered first project name')
    step_edit_project_name(proj)

    step_assert_two_projects(proj, another_proj, rp_logger)

    step_visit_edit_screen_of_project(index=another_index)

    step_assert_edit_screen_of_project(another_proj)

    another_proj = another_proj._replace(description='altered description')
    step_edit_project_description(another_proj)

    step_assert_two_projects(proj, another_proj, rp_logger)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    rp_logger.info('Verify that tapping on Delete Button will bring a confirmation dialog and by tapping on cancel '
                   'the Project remains intact and still present in the Dashboard')

    step_delete_project(index=index)

    dismiss_alert(mybrowser.driver)

    step_assert_two_projects(proj, another_proj, rp_logger)
    projs = [proj, another_proj]

    rp_logger.info(f'Creating a task for the project with index {index}')

    step_visit_add_task_of_project(mybrowser, index=index)

    step_assert_empty_add_task_form(mybrowser)

    some_basic_task = BasicTask(summary='temp summary', description='temp description')
    step_add_task(some_basic_task)

    step_assert_tasks_of_project_are_rendered(mybrowser)

    step_assert_single_basic_task(some_basic_task)

    step_access_dashboard_for_logged_in_user(mybrowser)

    rp_logger.info('Verify that tapping on Delete Button will bring a confirmation dialog and by accepting it will '
                   'remove the Project and all of its tasks from the Dashboard and by creating a new Project with the '
                   'exact same attributes (name and description) will yield an empty Project')

    step_delete_project(index=index)

    accept_alert(mybrowser.driver)

    step_visit_create_new_project()

    step_assert_create_project_screen_is_empty()

    step_fill_project_form(project=projs[index])

    step_submit_new_project_form()

    step_view_tasks_of_latest_project()

    step_assert_project_tasks_are_empty(mybrowser)

    rp_logger.info('Clearing all the projects to make this scenario be reusable due to using the same user')

    step_access_dashboard_for_logged_in_user(mybrowser)

    step_assert_two_projects(projs[another_index], projs[index], rp_logger)

    step_delete_all_projects(mybrowser)
