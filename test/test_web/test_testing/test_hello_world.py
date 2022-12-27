import pytest


@pytest.mark.issue(issue_id="111111", reason="Some bug", issue_type="PB")
@pytest.mark.hello_world
def test_user_invalid(users: dict):
    user = users['invalid']
    print(user['password'])
    # pytest.fail("we still need to implement this case")


@pytest.mark.hello_world
def test_nothing():
    print('testing nothing')


@pytest.mark.hello_world
# @pytest.mark.results(['Testplan - My Feature - ', ])
# # testplan id, attributes of testrun and results
@pytest.mark.parametrize("platform", ['Android', 'iOS'])
def test_params(platform):
    print(platform)
