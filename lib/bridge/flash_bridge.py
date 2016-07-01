# flash_bridge.py, p_video/lib/bridge/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from .. import err
from ..util import log

from . import handwich_bridge


def get_bridge(bridge):
    if bridge == 'handwich_bridge':
        return handwich_bridge.init_bridge
    else:	# unknow bridge
        log.e('unknow flash_bridge ' + str(bridge))
        raise err.ConfigError('flag_bridge.get_bridge', bridge)

# end flash_bridge.py


