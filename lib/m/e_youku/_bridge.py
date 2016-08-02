# _bridge.py, p_video/lib/m/e_youku/

from ...util import log
from ...bridge import flash_bridge

from . import var


def init(gvar):
    pass	# NOTE nothing to do here now

def parse(first_raw, filetype_list):
    # TODO error process
    
    # init handwich_bridge
    create = flash_bridge.get_bridge('handwich_bridge')
    h = create(var._HANDWICH_BRIDGE_CORE)
    
    # make req data
    to = {
        'raw' : first_raw, 
        'filetype_list' : filetype_list, 
    }
    # DEBUG log
    log.d('call handwich_bridge/doll_youku, ' + str(filetype_list))
    
    out = h.call_core('parse', a=[to])[1]
    # DEBUG
    log.d('parse -> ' + str(out))
    return out

# end _bridge.py


