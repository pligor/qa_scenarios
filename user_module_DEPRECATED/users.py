import pandas as pd

_filename = f'user_module/test_users.csv'
df = pd.read_csv(_filename, encoding='utf8', delimiter=',', index_col='key')
assert len(df.index.unique()) == len(df.index), \
    'keys being used in users.csv files should be unique, duplicated were detected'


class UsersMeta(type):
    def __getitem__(self, item):
        return df.loc[item]

    # Gets called when an attribute is accessed
    def __getattribute__(self, item):
        # print('__getattribute__ ', item)
        # Calling the super class to avoid recursion if necessary
        # super(Yeah, self).__getattribute__(item)
        return df.loc[item]


# class Users(object):
class Users(metaclass=UsersMeta):
    pass
