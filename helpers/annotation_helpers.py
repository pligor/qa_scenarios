import types

import allure
import reportportal_client
from appium import webdriver
from devtools_ai.appium import SmartDriver
from helpers import PROJECT_PATH
from helpers.pytest_helpers import get_func_reference
from functools import wraps

def scenario_step(func):
    return reportportal_client.step(allure.step(func))



def drive_smartly(devtools_api_key,
                  driver_instance=webdriver.Remote,
                  devtools_test_case_key='test_case_name'): # this is default as it is defined in https://www.dev-tools.ai/docs/appium-basic-test-case
    """NOTE: This decorator needs to be called right above the test function
    NOTE: To train using the interactive mode for the Smart Driver of the Devtools ai library you need to prepend DEVTOOLSAI_INTERACTIVE=TRUE as environment variable
    e.g. DEVTOOLSAI_INTERACTIVE=TRUE pytest ....
    here we have all the parameters of the decorator and these actually return a decorator"""

    def the_decorator(func):
        """here the only parameter is the function as this is the decorator"""
        assert type(func) == types.FunctionType, 'do not use the decorator to anything else than functions'
        assert func.__name__.startswith('test_'), 'this decorator is meant only to be called for test functions'
        # print('varnames', func.__code__.co_varnames)

        changed = False
        def try_change_param_once(param):
            if isinstance(param, driver_instance):
                nonlocal changed
                if changed:
                    raise Exception('the change is expected to be applied only once, now you have more than one')
                changed = True
                return SmartDriver(driver=param, api_key=devtools_api_key,
                                   initialization_dict={devtools_test_case_key: get_func_reference(func)})
            else:
                return param

        @wraps(func)
        def the_wrapper(*args, **kwargs):
            """here we use the args and kwargs that are called to the original function"""
            # print('old kwargs', kwargs.keys())
            # print('len old args', len(args))
            new_kwargs = dict([(key, try_change_param_once(val)) for key, val in kwargs.items()])
            new_args = [try_change_param_once(arg) for arg in args]
            # print('new kwargs', new_kwargs.keys())
            # print('len args', len(new_args))
            return func(*new_args, **new_kwargs)

        return the_wrapper

    return the_decorator

if __name__ == '__main__':
    def change_param(splitter='-'):
        def change_param_inner(func):
            assert type(func) == types.FunctionType
            print("Inside the Decorator: ")

            changed = False

            def try_change_param_once(param):
                if isinstance(param, str):
                    nonlocal changed
                    if changed:
                        raise Exception('the change is expected to be applied only once, now you have more than one')
                    changed = True
                    return param.split(splitter)
                else:
                    return param

            def inner_func(*args, **kwargs):
                print("Inside the Inner Function: ")
                print("'Decorated the function'")
                print(PROJECT_PATH)
                # perform this operation with function_name

                new_kwargs = dict([(key, try_change_param_once(val)) for key, val in kwargs.items()])

                new_args = [try_change_param_once(arg) for arg in args]

                print('new kwargs', new_kwargs.keys())
                print('len args', len(new_args))

                return func(*new_args, **new_kwargs)

            return inner_func

        return change_param_inner


    @change_param(splitter='-')
    def myfunc(obj, somearg, fullstr, another):
        return obj, somearg, fullstr, another


    print(myfunc(4, 5.6, fullstr='doki.mi-twra-pali', another={'he': 5}))
