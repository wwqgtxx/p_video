# __init__.py, p_video/lib/bridge/handwich_bridge/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from ... import err, util
from ...var import var
from ...util import log

from ._handwich_client import HandwichHost


def init_bridge(core):
    # create client and set config
    h = HandwichHost()
    s = var.feature['handwich_bridge_server']
    h.ip = s['ip']
    h.port = s['port']
    h.key = s['key']
    h.core_id = s['core'][core]
    
    # check bridge version
    # TODO error process
    version = h.get_version()
    log.i('handwich_bridge version: ' + str(version))
    
    # check core version
    # TODO error process
    info = h.call_core('about')
    if info[0] == 'ret':
        log.i('bridge_core: ' + info[1])
    else:	# err
        log.e('bridge_core [' + core + '] not avaliable, ' + str(info))
        raise err.ConfigError('handwich_bridge.core_about', core, info)
    # check pass
    return h

# end __init__.py


