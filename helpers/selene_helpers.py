from time import sleep
from typing import Tuple

from selene import have
from selene.core.entity import Element, Collection

import platform

from selenium.webdriver import Keys

from test.test_web.conftest import msec_BETWEEN_KEYBOARD_KEYS


def extract_selector(elem: Element) -> Tuple[str, str]:
    return eval(elem._locator._description[len('browser.element('):-len(')')])


def send_keys(elem: Element, characters: str, natural_speed=False,
              delay_ms_between_keys=msec_BETWEEN_KEYBOARD_KEYS):
    assert len(characters) > 0, "use non empty strings as input, otherwise use safe_clear_input_element directly"
    if natural_speed:
        sleep(delay_ms_between_keys / 1000.0)
        for cur_char in characters:
            elem.send_keys(cur_char)
            sleep(delay_ms_between_keys / 1000.0)
    else:
        elem.send_keys(characters)


def safe_clear_input_element(elem: Element):
    os_base = platform.system()

    if os_base == 'Darwin':
        elem.send_keys(Keys.COMMAND, 'a')
    else:
        elem.send_keys(Keys.CONTROL, 'a')

    elem.send_keys(Keys.DELETE)

    elem.clear()

    elem.should(have.value(''))

    # Not recommended as not real user actions
    # elem.set_value('')
