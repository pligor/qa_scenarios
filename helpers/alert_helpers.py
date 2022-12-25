from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.test_web.conftest import IMPLICIT_WAIT


def dismiss_alert(driver: WebDriver):
    WebDriverWait(driver, IMPLICIT_WAIT).until(EC.alert_is_present())
    driver.switch_to.alert.dismiss()
    WebDriverWait(driver, IMPLICIT_WAIT).until_not(EC.alert_is_present())


def accept_alert(driver: WebDriver):
    WebDriverWait(driver, IMPLICIT_WAIT).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    WebDriverWait(driver, IMPLICIT_WAIT).until_not(EC.alert_is_present())
