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
    'm_set_um' : False, 
    'm_set_vv' : False, 
    
    'm_auth_key' : '', 	# NOTE maybe the password of one video
    
    'm_set_locale_zh_tw' : False, 
    
    # TODO support set_flag_v
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
    'tvid' : 'data-player-tvid="([^"]+)"', 
    'vid'  : 'data-player-videoid="([^"]+)"', 
    
    # NOTE `aid` maybe empty
    'aid'  : 'data-player-albumid="([^"]+)"', 
    
    'flag_vv' : 'data-player-ismember="([^"]+)"', 	# TODO process this
}
_IGNORE_VID = ['aid']


_CODE_OK = {	# for check ok_code
    'info_vms' : 'A000000', 	# code : 'A000000'
    'url_file' : '', 	# TODO
}

# com.qiyi.player.core.Config.MIXER_VX_URL
_MIXER_VX_URL = 'http://cache.video.qiyi.com'
_MIXER_BACKUP_URL = 'http://211.151.158.155'
_VIP_AUTH_URL = 'http://api.vip.iqiyi.com/services/ckn.action'

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


