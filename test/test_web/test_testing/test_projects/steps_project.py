from logging import Logger

from selene import Browser, be, have, query
from selene.core.entity import Element

from helpers.alert_helpers import accept_alert
from helpers.annotation_helpers import scenario_step
from helpers.pmtool_form_helpers import naturally_fill_pmtool_input
from helpers.selene_helpers import extract_selector
from screens.testing_screens.project_screens import Project
from screens.testing_screens.dashboard_screen import create_project_button, single_project_title, single_project_description, \
    project_cards, single_project_edit_button, single_project_delete_button
from screens.testing_screens.project_screens.create_project_screen import new_project_submit_create_button, new_project_name_label, \
    new_project_name_field, new_project_description_label, new_project_description_field
from screens.testing_screens.project_screens.edit_project_screen import edit_project_description_label, edit_project_description_field, \
    edit_project_name_label, edit_project_submit_update_button, edit_project_name_field
from test.test_web.test_testing.test_dashboard_functionality.steps_dashboard import step_assert_dashboard_screen_is_rendered, \
    step_dashboard_is_empty


@scenario_step
def step_delete_all_projects(mybrowser: Browser):
    count = project_cards.get(query.size)
    # assert count == 2, f'alliws to count einai {count}'
    for ii in range(count, 0, -1):
        step_delete_project(index=0)

        accept_alert(mybrowser.driver)

        post_count = max(ii - 1, 1)  # because if no projects one card is rendered for welcome purposes
        project_cards.should(have.size(post_count))

    step_dashboard_is_empty()


@scenario_step
def step_edit_project_description(project: Project):
    naturally_fill_pmtool_input(label_elem=edit_project_description_label,
                                field_elem=edit_project_description_field,
                                characters=project.description)

    edit_project_submit_update_button.should(be.clickable).click()


@scenario_step
def step_edit_project_name(project: Project):
    naturally_fill_pmtool_input(label_elem=edit_project_name_label,
                                field_elem=edit_project_name_field,
                                characters=project.name)

    edit_project_submit_update_button.should(be.clickable).click()


@scenario_step
def step_assert_edit_screen_of_project(project: Project):
    edit_project_name_field.should(be.visible.and_(have.value(project.name)))
    edit_project_description_field.should(have.value(project.description).and_(be.visible))
    edit_project_submit_update_button.should(be.visible.and_(have.text('UPDATE')))


@scenario_step
def step_delete_project(index: int):
    project_cards.should(have.size_greater_than_or_equal(index + 1))

    card = project_cards[index]

    card.s(extract_selector(single_project_delete_button)).should(be.visible.and_(be.clickable)).click()


@scenario_step
def step_visit_edit_screen_of_project(index: int):
    project_cards.should(have.size_greater_than_or_equal(index + 1))

    card = project_cards[index]

    card.s(extract_selector(single_project_edit_button)).should(be.visible.and_(be.clickable)).click()


@scenario_step
def step_assert_two_projects(project1: Project, project2: Project, rp_logger: Logger):
    project_cards.should(have.size(2))

    proj_card1, proj_card2 = project_cards
    proj_card1: Element = proj_card1

    # TODO erase these lines after maturity
    # rp_logger.debug(f'locator value: {single_project_title._locator._description}')
    # rp_logger.debug(f'locator type: {type(single_project_title._locator._description)}')
    # string_tpl = single_project_title._locator._description[len('browser.element('):-len(')')]
    # rp_logger.debug(f'string TPL is: {string_tpl}')
    # tpl = eval(string_tpl)
    # rp_logger.debug(f'TPL is: {tpl}')

    proj_card1.s(extract_selector(single_project_title)).should(have.text(project1.name))
    proj_card1.s(extract_selector(single_project_description)).should(have.text(project1.description))

    proj_card2.s(extract_selector(single_project_title)).should(have.text(project2.name))
    proj_card2.s(extract_selector(single_project_description)).should(have.text(project2.description))


@scenario_step
def step_create_new_project_from_dashboard(mybrowser: Browser, project: Project):
    step_assert_dashboard_screen_is_rendered(mybrowser)

    step_visit_create_new_project()

    step_assert_create_project_screen_is_empty()

    step_fill_project_form(project=project)

    step_submit_new_project_form()


@scenario_step
def step_assert_single_project_in_dashboard(project: Project):
    single_project_title.should(be.visible.and_(have.exact_text(project.name)))
    single_project_description.should(be.visible.and_(have.exact_text(project.description)))


@scenario_step
def step_submit_new_project_form():
    new_project_submit_create_button.should(be.clickable).click()


@scenario_step
def step_fill_project_form(project: Project):
    naturally_fill_pmtool_input(label_elem=new_project_name_label,
                                field_elem=new_project_name_field,
                                characters=project.name)

    naturally_fill_pmtool_input(label_elem=new_project_description_label,
                                field_elem=new_project_description_field,
                                characters=project.description)


@scenario_step
def step_assert_create_project_screen_is_empty():
    new_project_name_field.should(have.value('').and_(be.visible))
    new_project_description_field.should(have.value('').and_(be.visible))
    new_project_submit_create_button.should(be.visible.and_(have.text('CREATE')))


@scenario_step
def step_visit_create_new_project():
    create_project_button.should(be.clickable).click()
