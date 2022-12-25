import os

import pytest
from selene.support.shared import browser
from selene import Browser, Config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from fake_useragent import UserAgent
from fp.fp import FreeProxy
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def mybrowser(implicit_wait: int, is_headless: bool, current_base_url: str) -> Browser:
    os.environ['WDM_SSL_VERIFY'] = '0'  # if you attempt to download any new browsers do not care for SSL

    service = ChromeService(executable_path=
                            ChromeDriverManager().install()
                            # '/Users/student/selenium_drivers/chromedriver'
                            )
    options = webdriver.ChromeOptions()
    options.headless = is_headless
    options.add_argument("window-size=1400,800")
    driver = webdriver.Chrome(service=service, options=options)

    # TODO if you want to be undetected by Chrome follow instructions here: https://www.youtube.com/watch?v=eqTBZxGNwAs
    # driver = WebDriver().get_driver()

    config = Config(
        driver=driver,
        base_url=current_base_url,
        timeout=implicit_wait,  # Configuration.IMPLICIT_WAIT,
        wait_for_no_overlap_found_by_js=True,
    )

    # browser.config.browser_name = 'chrome' #unnecessary since we set the driver explicitly
    browser.config.base_url = config.base_url
    browser.config.timeout = config.timeout
    browser.config.wait_for_no_overlap_found_by_js = config.wait_for_no_overlap_found_by_js
    browser.config.driver = config.driver
    # TODO if you want to use your own instance, and not the shared one provided, but not sure how to integrated it yet
    # browser = Browser(config)

    return browser


@pytest.fixture(autouse=True, scope='function')
def terminator(mybrowser, rp_logger):
    yield  # execute the function first
    rp_logger.debug("terminating browser")  # debug messages are logged but will NOT be sent to Report Portal
    mybrowser.quit()


class Spoofer(object):

    def __init__(self, country_id=('GR',), rand=True, anonym=True):
        self.country_id = country_id
        self.rand = rand
        self.anonym = anonym
        self.userAgent, self.ip = self.get()

    def get(self):
        ua = UserAgent()
        proxy = FreeProxy(country_id=self.country_id, rand=self.rand, anonym=self.anonym).get()
        ip = proxy.split("://")[1]
        return ua.random, ip


class DriverOptions(object):

    def __init__(self):
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")

        self.helperSpoofer = Spoofer()

        self.options.add_argument('user-agent={}'.format(self.helperSpoofer.userAgent))
        self.options.add_argument('--proxy-server=%s' % self.helperSpoofer.ip)


class WebDriver(DriverOptions):

    def __init__(self, path=''):
        DriverOptions.__init__(self)
        self.driver_instance = self.get_driver()

    def get_driver(self):
        # print("""
        # IP:{}
        # UserAgent: {}
        # """.format(self.helperSpoofer.ip, self.helperSpoofer.userAgent))

        proxy = self.helperSpoofer.ip
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy,
            "noProxy": None,
            "proxyType": "MANUAL",
            "autodetect": False
        }
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

        # path = os.path.join(os.getcwd(), '../windowsDriver/chromedriver.exe')
        # driver = webdriver.Chrome(executable_path=path, options=self.options)
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=self.options)

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })

        return driver
