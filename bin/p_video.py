#!/usr/bin/env python3.5
# p_video.py, p_video/bin/

# TODO LICENSE info

import os, sys

def get_root_path():
    now_file = __file__
    bin_file = os.path.realpath(now_file)
    now_dir = os.path.dirname(bin_file)
    root_dir = os.path.join(now_dir, '../')
    return root_dir

sys.path.insert(0, get_root_path())

from lib.cli import about, help, p_arg, use_arg
from lib import err, util, cache
from lib.util import log
from lib.var import var


def main(argv):
    # parse CLI arguments
    arg_info = p_arg.parse(argv)
    
    # TODO FIXME DEBUG here
    
    # TODO


if __name__ == '__main__':
    exit(main(sys.argv[1:]))
# end p_video.py


