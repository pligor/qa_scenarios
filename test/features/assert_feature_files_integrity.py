import re
import glob
from pathlib import Path
current_folder = globals()['_dh'][0] if '_dh' in globals() else Path(__file__).parent

prio_tag_prefix = 'prio'

priority_tags = [f'{prio_tag_prefix}_{prio}' for prio in ['trivial', 'minor', 'major', 'critical']]

def act_on_every_file(root_dir, func=print, ext='feature', debug=False):
    # root_dir needs a trailing slash (i.e. /root/dir/)
    root_dir = str(root_dir)
    root_dir = root_dir if root_dir[-1] == '/' else root_dir + '/'
    for filename in glob.iglob(root_dir + f'**/*.{ext}', recursive=True):
        if debug:
            print(filename)
        func(filename)


def assert_single_feature_per_file(filename):
    with open(filename) as fp:
        lines = fp.readlines()

    assert sum([line.strip().lower().startswith('feature') for line in lines]) == 1, \
        f'file "{filename}" has more than one features in a single file violating the Gherkin convention'

def assert_all_comments_in_separate_line(filename, comment_pattern = re.compile('\s#.*')):
    with open(filename) as fp:
        lines = fp.readlines()

    assert sum([(comment_pattern.search(line) is not None) for line in lines if not line.strip().startswith('#')]) == 0, \
        f'file "{filename}" has the comment hashtag symbol(#) in a line that is not strictly for a comment. Put comments in their own lines as they are not parsed'


def assert_only_valid_priority_tags_are_used(filename, prio_tags = priority_tags, prio_tag_prefix = prio_tag_prefix):
    with open(filename) as fp:
        lines = fp.readlines()
    
    check = lambda ll: [prio_tag in ll for prio_tag in prio_tags]
    
    prio_tag_prefix = prio_tag_prefix if prio_tag_prefix.startswith('@') else f'@{prio_tag_prefix}'  # append @ at first if necessary
    for ll in [line for line in lines if prio_tag_prefix in line]:
        assert ll.count(prio_tag_prefix) == 1, \
            f'do not use more than one priority for a single scenario and now you have used more than in a single line in file {filename} for line {ll}'
        assert sum(check(ll)) == 1, \
            f'only one of the valid priorities are expected to exist in a line with a priority tag for file {filename} for line {ll}'

