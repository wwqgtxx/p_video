# var.py, p_video/lib/
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

from .conf import get_feature_init

# pvinfo const
PVINFO_MARK_UUID = 'fa8b4922-983f-4bca-8127-9028055fad89'
PVINFO_PORT_VERSION = '0.8.0-1'


class GVar(object):
    '''
    p_video global data
    
    NOTE data from command line arguments or stdin will be directly here
    '''
    def __init__(self):
        # init feature value (default)
        self.feature = get_feature_init()
        
        # command line data
        self.debug = False	# --debug, global debug (low-level) flag
        
        self.module = None	# -m, --module MODULE
        self.entry = None	# -e, --entry ENTRY
        
        self.rest = []	# --, rest command line arguments
        self.raw_url = []	# raw input URLs
        
        self.raw_cli_config = {}	# raw command line config object to output (pvinfo)
        
        # raw stdin data
        self.raw_stdin = None
        self.raw_json = None	# json data input from stdin
        
        self.cache = {}		# global module/entry cache
        # NOTE single module in p_video process
        self.mvar = None	# module var object
        self.e = {}		# module/entry class
        
        # output (print stdout) result flag
        self.pretty_print_sort_key = True	# json.dumps(sort_keys=), should set to false after pretty_print restruct (OrderedDict)
    # end GVar class

var = GVar()	# exports
# end var.py


