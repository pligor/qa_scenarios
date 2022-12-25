from logging import Logger
from os.path import isfile
from pathlib import Path
from subprocess import Popen
from os import environ
import pytest
from appium import webdriver
from devtools_ai.appium import SmartDriver

from helpers.cmd_helper import get_android_adb_device

@pytest.fixture(scope='session')
def app_id() -> str:
    return 'com.immr.immrtodolist'

def new_command_timeout(rp_logger: Logger) -> int:
    """https://www.dev-tools.ai/docs/appium-interactive-mode"""
    new_command_timeout = 600 if environ.get('DEVTOOLSAI_INTERACTIVE') == 'TRUE' else 60
    rp_logger.info(f'Setting new command timeout to {new_command_timeout}')
    return new_command_timeout

@pytest.fixture(scope='function')
def driver(app_id: str, rp_logger: Logger, implicit_wait: int, appium_process: Popen) -> webdriver.Remote:
    # print('\nsetup_function()')
    rp_logger.info("Initializing TODO app")

    apk_path = (Path(__file__).parent / Path("apps/android/todo_immr_resource_ids.apk")).resolve()
    assert isfile(apk_path), f"apk path should be a valid file, currently is {apk_path}"

    # for already existing app we need these capabilities https://discuss.appium.io/t/android-launch-already-installed-app/5020/2
    desired_caps = {
        # "build": "Python Android",
        # "device": "Samsung Galaxy S8 Plus",
        # "app": "<app_url>"
        "platformName": "Android",
        "deviceName": get_android_adb_device(),
        "appPackage": app_id,
        "app": str(apk_path),
        # "appActivity": initial_android_app_activity(),
        "automationName": "UiAutomator2",
        "newCommandTimeout": new_command_timeout(rp_logger),
    }

    rp_logger.info(f"Desired Capabilities: {desired_caps}")

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(implicit_wait)

    return driver


@pytest.fixture(autouse=True, scope='function')
def terminator(driver: webdriver.Remote, app_id, rp_logger: Logger):
    yield  # execute the function first
    rp_logger.info("terminating app")
    try:
        terminated = driver.terminate_app(app_id=app_id)
        assert terminated, "app is expected to be terminated successfully upon finish of one scenario"
    finally:
        driver.quit()
