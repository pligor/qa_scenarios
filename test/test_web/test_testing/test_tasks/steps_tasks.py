from selene import Browser, be, have, by
from selene.support.shared.jquery_style import ss

from helpers.annotation_helpers import scenario_step
from helpers.pmtool_form_helpers import naturally_fill_pmtool_input
from helpers.selene_helpers import extract_selector
from screens.testing_screens.dashboard_screen import project_cards, single_project_add_task_button, \
    single_project_view_tasks_button
from screens.testing_screens.task_screens import BasicTask
from screens.testing_screens.task_screens.create_task_screen import new_task_summary_label, new_task_summary_field, \
    new_task_description_label, new_task_description_field, new_task_submit_create_button, new_task_status_field
from screens.testing_screens.task_screens.tasks_screen import task_edit_button, task_delete_button, \
    task_summary_title, task_description_text, todo_column_header, in_progress_column_header, in_review_column_header, \
    done_column_header, get_column_container_by_task_status, task_title_css_selector
from test.test_web.test_testing.test_dashboard_functionality.steps_dashboard import step_assert_dashboard_screen_is_rendered


@scenario_step
def step_assert_project_tasks_are_empty(mybrowser: Browser):
    step_assert_tasks_of_project_are_rendered(mybrowser)

    for elem in [task_summary_title, task_description_text, task_edit_button, task_delete_button]:
        ss(extract_selector(elem)).should(be.empty)


@scenario_step
def step_view_tasks_of_latest_project():
    project_cards.should(have.size_greater_than_or_equal(1))
    latest_card = project_cards[-1]
    latest_card.s(extract_selector(single_project_view_tasks_button)).should(be.visible.and_(be.clickable)).click()


@scenario_step
def step_assert_single_basic_task(basic_task: BasicTask):
    task_edit_button.should(be.visible)

    task_delete_button.should(be.visible)

    task_summary_title.should(be.visible.and_(have.exact_text(basic_task.summary)))

    task_description_text.should(be.visible.and_(have.exact_text(basic_task.description)))


@scenario_step
def step_assert_tasks_of_project_are_rendered(mybrowser: Browser):
    mybrowser.should(have.url_containing('/projects').and_(have.url_containing('/tasks')))

    todo_column_header.should(have.exact_text('TO DO').and_(be.visible))

    in_progress_column_header.should(have.exact_text('IN PROGRESS').and_(be.visible))

    in_review_column_header.should(have.exact_text('IN REVIEW').and_(be.visible))

    done_column_header.should(have.exact_text('DONE').and_(be.visible))


@scenario_step
def step_assert_status_column_has_tasks(status_column: str, task_names: list[str]):
    col_container = get_column_container_by_task_status(status_column)
    tasks = col_container.ss(by.css(task_title_css_selector))

    tasks.should(have.size(len(task_names)))

    # queried_names = [task.get(query.text) for task in tasks] #use if you need to be more relaxed
    tasks.should(have.exact_texts(*task_names))  # this takes into account the order of the items


@scenario_step
def step_add_task(basic_task=BasicTask):
    naturally_fill_pmtool_input(label_elem=new_task_summary_label,
                                field_elem=new_task_summary_field,
                                characters=basic_task.summary)

    naturally_fill_pmtool_input(label_elem=new_task_description_label,
                                field_elem=new_task_description_field,
                                characters=basic_task.description)

    new_task_submit_create_button.should(be.clickable.and_(have.text('CREATE'))).click()


@scenario_step
def step_assert_empty_add_task_form(mybrowser: Browser):
    mybrowser.should(have.url_containing('/createTask'))
    new_task_summary_field.should(have.value(''))
    new_task_description_field.should(have.value(''))
    new_task_status_field.should(have.value('TO DO'))


@scenario_step
def step_visit_add_task_of_project(mybrowser: Browser, index: int):
    step_assert_dashboard_screen_is_rendered(mybrowser)

    project_cards.should(have.size_greater_than_or_equal(index + 1))

    card = project_cards[index]

    card.s(extract_selector(single_project_add_task_button)).should(be.visible.and_(be.clickable)).click()
