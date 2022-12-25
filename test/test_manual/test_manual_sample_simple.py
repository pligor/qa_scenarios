from pytest_bdd import scenario, given, when, then, scenarios, parsers
from pathlib import Path
from os.path import isfile

cwd = Path(__file__).resolve().parent
FEATURE_FILE = str(Path(f'{cwd.parent}/features/sample_feature.feature').resolve())
assert isfile(FEATURE_FILE)
scenarios(FEATURE_FILE)

# exec("test_0 = mark_scenario(FEATURE_FILE, 'Verify some thing', True)")
# exec("test_1 = mark_scenario(FEATURE_FILE, 'Verify some other thing which fails', False, 'Result failed badly')")

# test_0 = mark_scenario(FEATURE_FILE, 'Verify some thing', True)
# test_1 = mark_scenario(FEATURE_FILE, 'Verify some other thing which fails', True, 'Result failed badly')

# @given('the specified conditions')
# def sample_given():
#     pass
#
#
# @when('the user is executing the action')
# def sample_when():
#     pass
#
#
# @then('some results are expected')
# def sample_then():
#     pass
