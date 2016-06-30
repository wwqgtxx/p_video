#!/usr/bin/env python3.5
# p_video.py, p_video/bin/
#
#    p_video : parse to get video info from some web sites. 
#    Copyright (C) 2016 sceext <sceext@foxmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>. 
#

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


