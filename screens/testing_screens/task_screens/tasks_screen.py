from selene import by, be, have, query
from selene.core.entity import Collection, Element
from selene.support.shared.jquery_style import s, ss

task_title_css_selector = "span#card_title"

task_summary_title = s(by.css(task_title_css_selector))

task_description_text = s(by.css("p#card_description"))

task_edit_button = s(by.css("a#btn_update_task"))

task_delete_button = s(by.css("a#btn_delete_task"))

todo_column_header = s(by.css(".s3:nth-of-type(1) h6"))

in_progress_column_header = s(by.css(".s3:nth-of-type(2) h6"))

in_review_column_header = s(by.css(".s3:nth-of-type(3) h6"))

done_column_header = s(by.css(".s3:nth-of-type(4) h6"))


def get_task_cards_by_name_xpath(task_name: str) -> str:
    assert not ('"' in task_name and "'" in task_name), \
        "do not have both single quote and double quote in the name. " \
        "If you are forced to follow the concat solution like so https://stackoverflow.com/a/14822893/720484"
    mychar = '"' if "'" in task_name else "'"
    return f"//span[text()={mychar}{task_name}{mychar}]/parent::div/parent::div"
    # return f"//span[text()={mychar}{task_name}{mychar}]"


def get_task_cards_by_name(task_name: str):
    return ss(by.xpath(get_task_cards_by_name_xpath(task_name)))


in_review_container_xpath = '//div[@id="in_review_items"]'

todo_container = s(by.css('div#to_do_items'))
in_progress_container = s(by.css('div#in_progress_items'))
in_review_container = s(by.css('div#in_review_items'))

def get_column_container_by_task_status(status: str) -> Element:
    status = status.lower().replace(' ', '')
    dic = {
        'todo': 'to_do_items',
        'inprogress': 'in_progress_items',
        'inreview': 'in_review_items',
        'done': 'done_items',
    }
    return s(by.css('#' + dic[status]))
