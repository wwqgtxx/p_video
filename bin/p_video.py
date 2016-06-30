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


def start_normal(arg_info):
    
    # FIXME TODO
    _print_bad_cli()
    # TODO


def _print_help(help_item):
    # TODO support help_item
    print(help.get_help())

def _print_bad_cli():
    log.e('bad command line, please try "--help"')

def main(argv):
    # parse CLI arguments
    log.log_module = True
    log.log_function = False
    try:
        arg_info = p_arg.parse(argv)
    except Exception as e:
        _print_bad_cli()
        return 1
    log.log_module = False
    
    # TODO process low-level debug (--debug)
    if arg_info['_debug']:
        log.d('low-level: arg_info ' + util.json_print(arg_info))
        # TODO maybe set to global var
    
    # check start mode
    sm = arg_info['_start_mode']
    if sm == '--help':
        _print_help(arg_info['_help_item'])
    elif sm == '--version':
        print(about.get_version_info())
    elif sm == '--license':
        print(about.get_license())
    else:	# (sm == '') normal start
        return start_normal(arg_info)
    return 0

if __name__ == '__main__':
    exit(main(sys.argv[1:]))
# end p_video.py


