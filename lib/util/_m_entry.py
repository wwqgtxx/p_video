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

class MEntry(object):
    def __init__(self):
        self.gvar = None
    
    def get_dep(self, gvar, data):
        self.gvar = gvar
        
        return []
    
    def do_p(self, data):
        raise NotImplementedError
    
    
    @staticmethod
    def _get_key_data(key, data_item):
        for i in data_item:
            if i['key'] == key:
                return i['ret']
        return None
    
    # end MEntry class


# end _m_entry.py


