import types
from helpers import PROJECT_PATH
from helpers.string_helpers import convert_any_text_to_separated_words


def get_func_reference(func):
    assert type(func) == types.FunctionType
    func_ref = f"{func.__code__.co_filename[len(str(PROJECT_PATH))+1:]}::{func.__name__}"
    return convert_any_text_to_separated_words(func_ref)


if __name__ == '__main__':
    def funcy():
        print('Here')

    aa = "var"

    if type(funcy) == types.FunctionType:
        print('It is a function')
    else:
        print('It is not a function')

    print(get_func_reference(funcy))
