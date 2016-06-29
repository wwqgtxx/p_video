# key_vf.py, p_video/lib/m/e_271/

import re

from ... import err, net
from ...util import log, MEntry

from . import var, _bridge


class Entry(MEntry):
    '''
    module/entry: m.e_271.key_vf
    
    data : {
        '_raw' : '', 	# raw str to get key_vf
    }
    
    -> '' (str) vf
    '''
    # no dep
    
    def do_p(self, data):
        raw_str = data
        # init bridge
        _bridge.init(self.gvar)
        
        vf = _bridge.get_vf(raw_str)
        return vf
    # end Entry class

module_entry = Entry
# end key_vf.py


