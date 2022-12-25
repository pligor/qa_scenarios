from pathlib import Path
from test.test_manual import mark_scenario, scenario_to_test_func_name, validate_results_uniqueness, process_result
assert mark_scenario is not None


FEATURE_FILE = str(Path(f'{Path(__file__).resolve().parent}/../features/sample_feature.feature').resolve())

results = [
    ['Verify some thing', None],
    ['Verify some other thing'],
    ['Some Sample Scenario title', 'Result failed badly'],
]

for result in validate_results_uniqueness(results):
    is_pass, reason = process_result(result)
    exec(f"{scenario_to_test_func_name(result[0])} = mark_scenario(FEATURE_FILE, '{result[0]}', {is_pass}, {reason})")
