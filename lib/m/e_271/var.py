# var.py, p_video/lib/m/e_271/
# extractor module: 271

from ...util import MVar
from ...util import log


# module const

SITE = '271'
SITE_NAME = '不可说'

RE_SUPPORT_URL = [
    # http://www.iqiyi.com/v_19rrlagk6k.html
    '^http://[a-z]+\.iqiyi\.com/.+\.html', 
]

MODULE_FEATURES = {	# module support features and init value
    # TODO
}
CACHE_BLACKLIST = [	# never cache these items (entry)
    'key_vf', 
    'url_before', 
    'url_file', 
    'vv_key', 
]

# at 2016-06-29
_SWF_PLAYER = 'http://www.iqiyi.com/common/flashplayer/20160620/1719f98c2359.swf'
_HANDWICH_BRIDGE_CORE = 'kill_271_cmd5'

# parse const

_RE_VID = {
    # TODO
}

# TODO


class Var(MVar):
    '''
    module global var and init
    '''
    def __init__(self, var):
        super().__init__(var)
        
        # TODO check and init module features
        
        # TODO init cache (use) list
        
        # TODO
    # end Var class

module_var = Var	# exports
# end var.py


