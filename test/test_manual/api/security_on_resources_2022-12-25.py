# ./pytest_script/pytest_manual.py test/test_manual/api/security_on_resources_2022-12-25.py

from test.test_manual import mark_scenario, scenario_to_test_func_name, validate_results_uniqueness, process_result
assert mark_scenario is not None
from os.path import isfile

FEATURE_FILE = '/Users/gp/Dropbox/projects/qa_scenarios/test/features/api/security_on_resources.feature'
assert isfile(FEATURE_FILE)

results = [
['''Verify that using a user who has not verified his/her email address but is attempting to verify his/her mobile phone number, this will yield a corresponding error message that will explain to the user of what actions he/she needs to take in order to proceed with the verification of the mobile phone number''', None],
['''Verify that a user who has verified his/her email address when attempting to verify his/her mobile phone number, this will be successful given that the phone number is valid and the 4 digit code that the user received as OTP was used properly''', None],
['''Verify that a user who has logged in using any Social Network, who has not yet verified his phone number, he is allowed to verify his a phone number''', None],
['''Verify that a user who has not verified his phone number when attempting either from the Report button of the Home screen or from the plus-icon button of MyCity screen, he will receive an error message explaining to him that first his phone number needs to be verified before submitting any report''', None],
['''Verify that a user who has already verified his phone number, even if he updated his email and currently is pending for verification, he will still be allowed to send as many Reports as he wishes to''', None],
['''Verify that for a single user, who has already executed 10 requests for verification of any email addresses, executing an 11th request for verification of an email address, within a month should NOT be allowed, and the user should receive an error message explaining to him when the next attempt to verify an email address can happen''', None],
['''Verify that for a single user, executing 10 requests for verification of some phone number, within a month should be allowed''', None],
['''Verify that for a single user, who has executed 9 requests for verification of some email addresses, plus 9 requests for verification of some phone numbers, then attempting to execute a 10th request for the verification of an email address should be allowed''', None],
['''Verify that for a single user, who has executed 10 requests for verification of some email addresses, plus 9 requests for verification of some phone numbers, should NOT be allowed to execute a verification of an email address but should be allowed to execute a verification of some phone number''', None],
['''Verify that for a single user, who has executed 10 requests for verification of some email addresses, plus 10 requests for verification of some phone numbers, should NOT be allowed to execute a verification of an email address NOR he should be allowed to execute a verification of any phone number, for within the month''', None],
['''Verify that for a single user, who has executed 10 requests for verification of some email addresses, plus 10 requests for verification of some phone numbers, if the period of the One Month has passed, then the user will be allowed to execute a verification both for some email address and for some phone number''', None],
['''Verify that a user who had verify his/her email address, but has changed his/her email address, and thus this is deemed as no longer valid, if he has not yet verified his phone number, he will NOT be allowed to verify it until the new/updated email is also verified''', None],
['''Verify that a user who had verify his/her email address, but has changed his/her email address, and thus this is deemed as no longer valid, if he had already verified his phone number, then he will NOT be forced to verify his phone number once more''', None],
['''Verify that a user who has logged in using any Social Network, who has already verified his phone number, he is allowed to verify a second phone number given, which will replace the first one''', None],
['''Verify that a user who has logged in using any Social Network, who has already verified his phone number, then this user is allowed to create/file as many Reports as he wishes to''', None],
['''Verify that for a single user, executing 10 requests for verification of some email addresses, within a month should be allowed''', None],
['''Verify that for a single user, who has already executed 10 requests for verification of any phone numbers, executing an 11th request for verification of a phone number, within a month should NOT be allowed, and the user should receive an error message explaining to him when the next attempt to verify his phone number can happen''', None],
['''Verify that a user who has logged in using any Social Network, who has not yet verified his phone number, then this user is NOT allowed to create/file any Report''', None],
['''Verify that a user who has already verified his phone number, if he attempts to reverify the exact same phone numbers, an informative message should explain to the user that he cannot re-verify the same phone number or he will not be able to proceed with the verification of the phone number at all (the submit button will be disabled)''', None],
]

for result in validate_results_uniqueness(results):
    is_pass, reason = process_result(result)
    exec(f"{scenario_to_test_func_name(result[0])} = mark_scenario(FEATURE_FILE, '''{result[0]}''', {is_pass}, {reason})")
