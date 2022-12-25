from selenium import webdriver


class Screen(object):
    def __init__(self, driver: webdriver.Chrome) -> None:
        super().__init__()
        self.driver = driver
