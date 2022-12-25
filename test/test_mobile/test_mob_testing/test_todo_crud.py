from logging import Logger
from time import sleep
from typing import Final

import pytest
from appium.webdriver import WebElement
from devtools_ai.appium import SmartDriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .constants import devtools_api_key
from helpers.annotation_helpers import drive_smartly

# @drive_smartly(devtools_api_key)
@pytest.mark.parametrize('task_name,description', [
    ['Name of Smart Todo Item', 'My Smart Description is here'],
])
@drive_smartly(devtools_api_key)
def test_smart_todo_create(task_name: str, description: str, driver: SmartDriver, rp_logger: Logger):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        [MobileBy.ID, 'btnAddNotes']))

    sleep(1) # as the dev-tools.ai/docs/appium-find-by-ai example suggests use a sleep before any find by ai call
    btn_add_notes: Final[WebElement] = driver.find_by_ai('btn_add_notes') #id btnAddNotes
    WebDriverWait(driver, 10).until(EC.visibility_of(btn_add_notes))

    assert btn_add_notes.text == 'TAMMBAH'
    btn_add_notes.click()

    sleep(1) # as the dev-tools.ai/docs/appium-find-by-ai example suggests use a sleep before any find by ai call
    input_title = driver.find_by_ai('input_title') # [MobileBy.ID, 'inputTitle']
    WebDriverWait(driver, 10).until(EC.visibility_of(input_title))

    input_title.send_keys(task_name)

    sleep(1) # as the dev-tools.ai/docs/appium-find-by-ai example suggests use a sleep before any find by ai call
    input_desc = driver.find_by_ai('input_desc')  # [MobileBy.ID, 'inputDesc']
    WebDriverWait(driver, 10).until(EC.visibility_of(input_desc))

    input_desc.send_keys(description)

    driver.hide_keyboard()

    sleep(1) # as the dev-tools.ai/docs/appium-find-by-ai example suggests use a sleep before any find by ai call
    btn_add = driver.find_by_ai('btn_add')  # [MobileBy.ID, 'btnAdd']
    WebDriverWait(driver, 10).until(EC.visibility_of(btn_add))

    assert btn_add.text == 'SIMPAN'
    btn_add.click()

    sleep(1) # as the dev-tools.ai/docs/appium-find-by-ai example suggests use a sleep before any find by ai call
    title = driver.find_by_ai('title')  # [MobileBy.ID, 'title']
    WebDriverWait(driver, 10).until(EC.visibility_of(title))
    assert title.text == task_name

    sleep(1) # as the dev-tools.ai/docs/appium-find-by-ai example suggests use a sleep before any find by ai call
    desc = driver.find_by_ai('desc')  # [MobileBy.ID, 'desc']
    WebDriverWait(driver, 10).until(EC.visibility_of(desc))
    assert desc.text == description

    sleep(1) # as the dev-tools.ai/docs/appium-find-by-ai example suggests use a sleep before any find by ai call
    delete = driver.find_by_ai('delete')  # [MobileBy.ID, 'delete']
    WebDriverWait(driver, 10).until(EC.visibility_of(delete))
    delete.click()

@pytest.mark.parametrize('task_name,description', [
    ['Name of First Todo Item', 'My First Description is here'],
])
def test_todo_create(task_name: str, description: str, driver: SmartDriver, rp_logger: Logger):

    elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        [MobileBy.ID, 'btnAddNotes']))

    # elem = driver.find_element(By.ID, 'btnAddNotes')
    assert elem.text == 'TAMMBAH'

    elem.click()

    input_title: Final = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        [MobileBy.ID, 'inputTitle']))

    input_title.send_keys(task_name)

    input_desc: Final = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        [MobileBy.ID, 'inputDesc']))

    input_desc.send_keys(description)


    btn_add: Final = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        [MobileBy.ID, 'btnAdd']))
    assert btn_add.text == 'SIMPAN'
    btn_add.click()


    title: Final = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        [MobileBy.ID, 'title']))
    assert title.text == task_name

    desc: Final = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        [MobileBy.ID, 'desc']))
    assert desc.text == description

    delete: Final = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        [MobileBy.ID, 'delete']))
    delete.click()

