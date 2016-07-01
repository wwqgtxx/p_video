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
import json

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
from lib.var import var, PVINFO_MARK_UUID, PVINFO_PORT_VERSION


def _read_stdin():
    i = sys.stdin.buffer
    return i.read()

def start_normal(arg_info):
    # check --set-json
    module_raw = None	# _raw data for first module/entry
    if arg_info['_set_json']:
        blob = _read_stdin()
        var.raw_stdin = blob
        
        text = blob.decode('utf-8')
        info = json.loads(text)
        var.raw_json = info
        # check mark_uuid and port_version
        if ('mark_uuid' in info) and (info['mark_uuid'] != PVINFO_MARK_UUID):
            log.w('pvinfo.mark_uuid ' + info['mark_uuid'] + ' != ' + PVINFO_MARK_UUID)
        if ('port_version' in info) and (info['port_version'] != PVINFO_PORT_VERSION):
            log.w('pvinfo.port_version ' + info['port_version'] + ' != ' + PVINFO_PORT_VERSION)
        # set info
        if 'config' in info:
            log.i('use pvinfo.config from stdin before CLI')
            use_arg.use(info['config'])
        if '_raw' in info:
            module_raw = info['_raw']
        if '_cache' in info:
            var.cache = info['_cache']
    # NOTE  CLI should override --set-json
    use_arg.use(arg_info)	# set cli arg value
    
    # TODO support auto-set/default module/entry name
    # check module/entry name
    if var.module == None:
        log.e('not set module name')
        raise err.ConfigError('no_module_name', var.module)
    if var.entry == None:
        log.e('not set entry name')
        raise err.ConfigError('no_entry_name', var.entry)
    
    # TODO turn no log_module maybe BUG or improved
    # NOTE turn on log_module
    old_log_module = log.log_module
    log.log_module = True
    # import and call module
    result = cache.do_call_module(module_raw)
    # NOTE restore log_module
    log.log_module = old_log_module
    
    # print result
    f = var.feature
    pretty_print = f['pretty_print']
    fix_unicode = f['fix_unicode']
    sort_key = var.pretty_print_sort_key
    if pretty_print:
        text = util.json_print(result, sort_key=sort_key, fix_unicode=fix_unicode)
    else:
        text = json.dumps(result, ensure_ascii=fix_unicode)
    text += '\n'
    blob = text.encode('utf-8')
    
    sys.stdout.buffer.write(blob)
    sys.stdout.buffer.flush()
    # done


def _print_help(help_item):
    # TODO support help_item
    print(help.get_help())

def _print_bad_cli():
    log.e('bad command line, please try "--help"')

def main(argv):
    # check no arg
    if len(argv) < 1:
        _print_bad_cli()
        return 1
    # parse CLI arguments
    log.log_module = True
    log.log_function = False
    try:
        arg_info = p_arg.parse(argv)
    except Exception as e:
        _print_bad_cli()
        return 1
    log.log_module = False
    # process low-level debug (--debug)
    if arg_info['_debug']:
        log.d('low-level: arg_info ' + util.json_print(arg_info))
    
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


