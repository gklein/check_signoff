from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

from subprocess import check_output, CalledProcessError


def main(argv=None):
    retval = 0
    commit_msg_path = sys.argv[1]
    with open(commit_msg_path) as f:
        found = 'Signed-off-by: ' in f.read()
        if not found:
            retval = 1
            print("The current git commit message is missing a 'Signed-off-by:' section")
            print("Please recommit with 'git commit --amend --signoff'")

    return retval


if __name__ == '__main__':
    exit(main())