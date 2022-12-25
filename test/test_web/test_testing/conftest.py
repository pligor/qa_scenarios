import pytest
import pandas as pd
from pathlib import Path
from os import environ

ENVIRONMENT_VARIABLE_NAME = "ENVIRONMENT_NAME"

def pytest_runtest_setup(item):
    pass
    # print('this WAS CALLED')
    # marks = [mark for mark in item.iter_markers(name="parametrize")]
    # print(f'MARKS: {marks}')
    # if envnames:
    #     if item.config.getoption("-E") not in envnames:
    #         pytest.skip("test requires env in {!r}".format(envnames))


@pytest.fixture(scope="session")
def users(current_environment_name: str):
    _filename = Path(
        f'{Path(__file__).resolve().parent}/users/{current_environment_name}_users.csv').resolve()
    df = pd.read_csv(_filename, encoding='utf8', delimiter=',', index_col='key')
    assert len(df.index.unique()) == len(df.index), \
        'keys being used in users.csv files should be unique, duplicated were detected'

    return dict(list(df.iterrows()))


@pytest.fixture(scope="session")
def current_base_url(environments: dict, current_environment_name: str):
    return environments[current_environment_name]

@pytest.fixture(scope="session")
def environments():
    return {  # TODO note that the dev, staging, and production environments are imaginary and will not work
        'dev': 'https://dev-node-fs-app.herokuapp.com',
        'test': 'https://node-fs-app.herokuapp.com',
        'staging': 'https://staging-node-fs-app.herokuapp.com',
        'production': 'https://prod-node-fs-app.herokuapp.com',
    }

@pytest.fixture(scope="session")
def current_environment_name(environments: dict) -> str:
    host_name = environ.get(ENVIRONMENT_VARIABLE_NAME).lower()

    if host_name:
        if host_name not in environments:
            raise Exception(
                f"ENVIRONMENT_NAME environment variable needs to have one of these values: {environments.keys()}")
    else:
        raise Exception(f'You need to define Environment variable with name {ENVIRONMENT_VARIABLE_NAME}\n'
                        'For example in command line: MY_ENV_NAME=MY_VALUE pytest ...')

    return host_name
