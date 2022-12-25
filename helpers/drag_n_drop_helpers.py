import os
from logging import Logger
from selene import be
from selene.core.entity import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.pointer_actions
from js import JS_PATH


def drag_n_drop_from_to_selenium_NOT_WORKING(from_elem: Element, to_target_elem: Element, driver: WebDriver, logger: Logger):
    source_web_elem = from_elem()
    target_web_elem = to_target_elem()
    logger.info(f'Dragging element of location {source_web_elem.location} and size {source_web_elem.size}')
    logger.info(f'and dropping element to location {target_web_elem.location} and size {target_web_elem.size}')

    # attempt 1 failed
    # ActionChains(driver).drag_and_drop(source=from_elem(), target=to_target_elem()).perform()

    # attempt 2 failed
    # action: ActionChains = ActionChains(driver).\
    #     click(source_web_elem).pause(1).\
    #     click_and_hold(source_web_elem).\
    #     pause(2)
    # action = action.move_to_location(650, 300).pause(1)
    # # action.move_to_element(target_web_elem).perform()
    # action.release().pause(2).perform()

    # Alternative solutions:
    # Reverse engineer this https://github.com/timrsfo/se-drag-n-drop
    # Or reverse engineer this: https://github.com/SatoDeNoor/selen


def drag_n_drop_via_js(from_elem: Element, target_elem: Element, driver: WebDriver, logger: Logger):
    from_elem.should(be.visible)
    target_elem.should(be.visible)

    source_web_elem = from_elem()
    target_web_elem = target_elem()

    logger.info(f'Dragging element of location {source_web_elem.location} and size {source_web_elem.size}')
    logger.info(f'and dropping element to location {target_web_elem.location} and size {target_web_elem.size}')

    with open(os.path.join(JS_PATH, 'dnd.js'), 'r') as fp:
        drag_and_drop_js = fp.read()

    driver.execute_script(drag_and_drop_js + ";executeDnD(arguments[0], arguments[1]);",
                          source_web_elem, target_web_elem)

# if __name__ == '__main__':
#     print("dokimi")
#     print(JS_PATH)
#     with open(os.path.join(JS_PATH, 'dnd.js'), 'r') as f:
#         drag_and_drop_js = f.read()
#     print('JS_BELOW')
#     print(drag_and_drop_js)
