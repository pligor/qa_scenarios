from selene import have, query
from selene.core.entity import Element

from helpers.selene_helpers import send_keys, safe_clear_input_element


def naturally_fill_pmtool_input(label_elem: Element, field_elem: Element, characters: str):
    label_elem.click()
    if field_elem.get(query.value) == '':
        label_elem.should(have.css_class('active'))
    else:
        label_elem.should(have.css_class('active'))
        field_elem.click()
        safe_clear_input_element(field_elem)

    send_keys(field_elem, characters, natural_speed=True)
