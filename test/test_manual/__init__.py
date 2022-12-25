from pytest_bdd import scenario, given, when, then, scenarios, parsers
import pytest

from helpers.string_helpers import convert_any_text_to_separated_words

PREFIX_SCENARIO_FUNC_NAME = 'test_'
assert PREFIX_SCENARIO_FUNC_NAME.startswith('test')  # due to Pytest convention

def process_result(result):
    is_pass = len(result) == 1
    reason = None if is_pass else result[1]
    reason = reason if reason is None else f"'{reason}'"
    return is_pass, reason

def validate_results_uniqueness(results):
    assert len(set([scenario_to_test_func_name(result[0]) for result in results])) == len(results), \
        "the generated functions should be unique"
    return results


def scenario_to_test_func_name(
        scenario_title: str = '33Verify that yo. next % ch^al with @$ and 54 numeric things'):
    return PREFIX_SCENARIO_FUNC_NAME + convert_any_text_to_separated_words(scenario_title)


def mark_scenario(feature_file: str, scenario_str, result: bool, reason: str = None):
    """https://stackoverflow.com/a/27005560/720484"""

    @scenario(feature_file, scenario_str)
    def local_func():
        if not result and reason is None:
            pytest.skip(f'Skipping scenario {scenario_str} as untested')
        elif not result:
            pytest.fail(reason)

    return locals()['local_func']
