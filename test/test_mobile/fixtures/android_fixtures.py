from logging import Logger
from pathlib import Path
import pytest
from appium import webdriver
from os.path import isfile
from helpers.cmd_helper import get_android_adb_device


# def app_name():
#     return 'xmtrading' if Configuration.get_current_flavour_optional() == 'xmtd' else 'xm'


@pytest.fixture(scope='session')
def app_id() -> str:
    return 'com.company.dev'


def initial_android_app_activity():
    return 'com.company.MainActivity'


@pytest.fixture(scope='function')
def driver(app_id: str, rp_logger: Logger, implicit_wait: int) -> webdriver.Remote:
    """:return webdriver.Remote"""
    # print('\nsetup_function()')
    rp_logger.info("Initializing app")

    apk_path = (Path(__file__).parent / Path("../apps/android/some_app.apk")).resolve()
    assert isfile(apk_path), "apk path should be a valid file"

    # for already existing app we need these capabilities https://discuss.appium.io/t/android-launch-already-installed-app/5020/2
    desired_caps = {
        # "build": "Python Android",
        # "device": "Samsung Galaxy S8 Plus",
        # "app": "<app_url>"
        "platformName": "Android",
        "deviceName": get_android_adb_device(),
        "appPackage": app_id,
        "app": str(apk_path),
        "appActivity": initial_android_app_activity(),
        # "automationName": "UiAutomator2",
    }

    rp_logger.info(f"Desired Capabilities: {desired_caps}")

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(implicit_wait)

    return driver
