import shortuuid
import re

uuid_pattern = re.compile('^@C[A-Za-z0-9]{22}$')
def get_uuid_case():
    sample = '@C' + shortuuid.uuid()
    assert uuid_pattern.match(sample) is not None
    return sample

if __name__ == '__main__':
    print(get_uuid_case())
