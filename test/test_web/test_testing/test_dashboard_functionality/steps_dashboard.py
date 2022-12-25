from selene import Browser, have, be
from selene.support.shared.jquery_style import ss

from helpers.annotation_helpers import scenario_step
from helpers.selene_helpers import extract_selector
from screens.testing_screens.dashboard_screen import project_cards, single_project_title, single_project_description, \
    single_project_edit_button, single_project_delete_button, single_project_add_task_button, \
    single_project_view_tasks_button, create_project_button


@scenario_step
def step_dashboard_is_empty():
    project_cards.should(have.size(1))

    single_project_title.should(have.exact_text('Welcome!'))
    single_project_description.should(have.exact_text('There are no projects created yet. Start by creating some!'))

    for elem in [single_project_edit_button,
                 single_project_delete_button,
                 single_project_add_task_button,
                 single_project_view_tasks_button]:
        ss(extract_selector(elem)).should(be.empty)


@scenario_step
def step_assert_dashboard_screen_is_rendered(mybrowser: Browser):
    mybrowser.should(have.url_containing('/dashboard'))
    create_project_button.should(be.visible.and_(have.text('CREATE')))
