import pytest
from appium import webdriver

from swagger_client import Configuration
from utils.logger import Logger

from helpers.cmd_helper import get_ios_udid, get_ios_name,get_ios_version
from fixtures import IMPLICIT_WAIT

def app_name():
    return 'xmtrading' if Configuration.get_current_flavour_optional() == 'xmtd' else 'xm'


@pytest.fixture
def app_id():
    return f"com.{app_name()}.WebApp"


@pytest.fixture
def driver(app_id):
    """:return webdriver.Remote"""
    # print('\nsetup_function()')
    Logger.info("Initializing app")

    # https://ivantay2003.medium.com/appium-desired-capabilities-basic-cheat-sheet-to-launch-mobile-application-ios-android-75b664367031
    # for already existing app we need these capabilities
    desired_caps = {
        'deviceName': get_ios_name(),
        'bundleId': app_id,
        'udid': get_ios_udid(),
        'platformVersion': get_ios_version(),
        "platformName": "iOS",
        "automationName": "XCuiTest",
        # not sure how to set these two but do not seem important either
        # "xcodeOrgId": "123415151",
        # "xcodeSigningId": "iPhone Developer"
    }

    Logger.info(f"Desired Capabilities: {desired_caps}")

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(IMPLICIT_WAIT)

    return driver
