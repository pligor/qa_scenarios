from pytest_bdd import scenarios
import glob
from pathlib import Path
from os.path import isdir, isfile

from helpers.file_helpers import gather_every_file

cwd = Path(__file__).resolve().parent
feature_folder = str(Path(f'{cwd.parent}/features/').resolve())
assert isdir(feature_folder)

features = gather_every_file(feature_folder, ext='feature')
scenarios(*features)

# This needs to be used in pytest with the --collect-only otherwise it will find lots and lots of missing steps
# If one does not like this approach then he/she is forced to use the pytest bdd generator in order to generate
# the missing implementations pytest --generate-missing --feature test/features/ test/test_manual/
# More regarding the latter here: https://pypi.org/project/pytest-bdd/

# TODO provide a feature file as input and generate a testrun with all the scenarios in a pending state
