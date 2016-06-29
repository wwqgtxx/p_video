# info_vms.py, p_video/lib/m/e_271/

import re

from ... import err, net
from ...util import log, MEntry

from . import var, _common


def _make_first_url_for_vf(gvar, info_vid):
    
    # TODO
    pass

def _make_first_url(raw, vf):
    
    # TODO
    pass


class Entry(MEntry):
    '''
    module/entry: m.e_271.info_vms
    
    data : {
        '_raw' : {
            'url' : '', 	# raw html page url
        }, 
    }
    
    -> {} (json object) raw vms json info (not parse vms)
    '''
    
    def get_dep(self, gvar, data):
        super().get_dep(gvar, data)
        
        # check get info_vid (first)
        
        # TODO
    
    def do_p(self, data):
        
        # TODO
        pass
    # end Entry class

module_entry = Entry
# end info_vms.py


