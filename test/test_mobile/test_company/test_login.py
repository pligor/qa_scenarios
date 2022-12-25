from logging import Logger
from time import sleep
from appium import webdriver


def test_login(driver: webdriver.Remote, rp_logger: Logger):
    sleep(5)
