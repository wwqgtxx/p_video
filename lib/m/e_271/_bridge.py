# _bridge.py, p_video/lib/m/e_271/

from ...util import log
from ...bridge import flash_bridge

from . import var


def init(gvar):	# init bridge (handwich_bridge)
    # NOTE init() may be called many times
    pass	# NOTE not init it here

def get_vf(raw):
    # TODO error process
    
    # init handwich_bridge
    create = flash_bridge.get_bridge('handwich_bridge')
    h = create(var._HANDWICH_BRIDGE_CORE)
    # DEBUG log
    log.d('call handwich_bridge.core.kill_271_cmd5.calc, ' + str(raw))
    # call it
    out = h.call_core('calc', a=[raw, raw])[1]
    log.d('calc -> ' + str(out))
    return out


# end _bridge.py


