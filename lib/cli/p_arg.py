# p_arg.py, p_video/lib/cli/
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

import json

from ..util import log
from .. import err


def _parse_feature_str(raw):
    return [i.strip() for i in raw.split(',')]

def _parse_set_feature(raw):
    try:
        out = json.loads(raw)
    except Exception:
        out = raw
    return out


def parse(args):
    out = {
        # pvinfo.config items
        'module' : None, 
        'entry' : None, 
        
        'rest' : [], 
        'raw_url' : [], 
        
        'enable' : [], 
        'disable' : [], 
        'feature' : {}, 
        
        'comment' : [], 
        
        # other cli items
        '_start_mode' : '', 	# in ['' (normal), '--help', '--version', '--license']
        '_help_item' : None, 	# TODO support --help XXX
        
        '_set_json' : False, 	# --set-json
        '_debug' : False, 	# --debug
    }
    
    # scan each arg
    rest = args[:]
    while len(rest) > 0:
        one, rest = rest[0], rest[1:]
        if one in ['-s', '--set']:
            to, rest = rest[0], rest[1:]
            key, value = to.split('=', 1)
            out['feature'][key] = _parse_set_feature(value)
        elif one in ['-E', '--enable']:
            to, rest = rest[0], rest[1:]
            out['enable'] += _parse_feature_str(to)
        elif one in ['-D', '--disable']:
            to, rest = rest[0], rest[1:]
            out['disable'] += _parse_feature_str(to)
        elif one in ['-m', '--module']:
            to, rest = rest[0], rest[1:]
            if out['module'] != None:
                log.w('already set module = ' + str(out['module']) + ', now set to ' + str(to))
            out['module'] = to
        elif one in ['-e', '--entry']:
            to, rest = rest[0], rest[1:]
            if out['entry'] != None:
                log.w('already set entry = ' + str(out['module']) + ', now set to ' + str(to))
            out['entry'] = to
        elif one in ['-#', '--comment']:
            to, rest = rest[0], rest[1:]
            out['comment'].append(to)
        elif one in ['-j', '--set-json']:
            out['_set_json'] = True
        elif one in ['--debug']:
            out['_debug'] = True
        elif one in ['--']:	# rest arg
            out['rest'] += rest
            rest = []
        elif one in ['--help', '--version', '--license']:	# start MODEs
            if out['_start_mode'] != '':
                log.e('already set _start_mode = ' + out['_start_mode'])
                raise err.ConfigError('_start_mode', one, out['_start_mode'])
            out['_start_mode'] = one
            # check --help
            if (one == '--help') and (len(rest) > 0):
                out['_help_item'], rest = rest[0], rest[1:]
        else:	# raw_url
            out['raw_url'].append(one)
    return out


# end p_arg.py


