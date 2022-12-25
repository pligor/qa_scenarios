import glob
from pathlib import Path
from os.path import isdir, isfile


def gather_every_file(root_dir, ext: str = 'feature'):
    assert isdir(root_dir)
    filenames = []

    # root_dir needs a trailing slash (i.e. /root/dir/)
    root_dir = root_dir if root_dir[-1] == '/' else root_dir + '/'
    for filename in glob.iglob(root_dir + f'**/*.{ext}', recursive=True):
        assert isfile(filename)
        filenames.append(filename)

    return filenames
