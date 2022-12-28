import pytest


@pytest.mark.hello_world
def test_nothing():
    print('testing nothing')


@pytest.mark.hello_world
@pytest.mark.parametrize("myparam", ['this', 'that'])
def test_params(myparam):
    print(myparam)
    if myparam == 'that':
        pytest.fail('it fails when the myparam is "that"')
