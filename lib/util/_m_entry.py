# _m_entry.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 
'''
module/entry class

    MEntry.get_dep(self, gvar, data) <= data (json) format
    
    {
        '<ENTRY>' : [	# entry name
            {
                'key' : {}, 	# the key-object
                'ret' : {}, 	# data (result object) return by MEntry.do_p()
            }, 
        ], 
        
        '_raw' : {	# `raw` data passed to this entry
        
        }, 
    }
    
    MEntry.get_dep(self, gvar, data) -> return (json) format
    
    [
        {
            'entry' : '', 	# a entry name of this module
            'key' : {}, 	# (or None) a key-object (json_cmp) used with cache
            'raw' : {}, 	# raw data object passed to this entry
        }, 
    ]
    
    
    MEntry.do_p(self, data) <= data (json) format
    
    NOTE this format is the same with `data` in `MEntry.get_dep(self, gvar, data)`

'''

from ._common import json_cmp


class MEntry(object):
    def __init__(self):
        self.gvar = None
        
        self._key = None
    
    def get_dep(self, gvar, data):
        self.gvar = gvar
        
        return []
    
    def do_p(self, data):
        raise NotImplementedError
    
    
    @staticmethod
    def _get_key_data(key, data_item):
        for i in data_item:
            if json_cmp(i['key'], key):
                return i['ret']
        return None
    
    def _check_dep_key(self, entry_name, data):
        if (not entry_name in data) or (self._get_key_data(self._key, data[entry_name]) == None):
            return True
        return False
    
    # end MEntry class


# end _m_entry.py


