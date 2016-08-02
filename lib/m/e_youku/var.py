# var.py, p_video/lib/m/e_youku/
# extractor module: youku

from ...util import log, MVar


# module const

SITE = 'youku'
SITE_NAME = '优酷'

RE_SUPPORT_URL = [
    # http://v.youku.com/v_show/id_XMTYzMTY0OTM1Ng==.html
    '^http://v\.youku\.com/v_show/id_[A-Za-z0-9=]+\.html', 
]

# at 2016-08-02
_SWF_PLAYER = 'http://static.youku.com/v1.0.0642/v/swf/player_yknpsv.swf'
_HANDWICH_BRIDGE_CORE = 'doll_youku'

# parse const

_RE_VID = {
    'vid' : 'var videoId2= \'([A-Za-z0-9=]+)\';', 
}

_CODE_OK = {
    # TODO
}

_GET_JSON = 'http://play.youku.com/play/get.json'
_GET_FLV_PATH = 'http://k.youku.com/player/getFlvPath'

# stream_type to filetype, for parse
_TO_FILETYPE = {
    'flvhd' : 'flv', 
    'mp4hd' : 'mp4', 
    'mp4hd2' : 'hd2', 
    'mp4hd3' : 'hd3', 
}

# site video stream_type to p_video hd quality
_TO_HD = {
    'mp4hd3' : 4, 	# 1080p, 1920 x 1080
    'mp4hd2' : 2, 	# 720p, 1280 x 720
    'mp4hd' : 0, 	# 540p, 960 x 540
    'flvhd' : -1, 	# 360p, 640 x 360
}


class Var(MVar):
    '''
    module global var and init
    '''
    @staticmethod
    def get_module_feature_init():
        out = {
            
            'm_cache_blacklist' : [
                'url_file', 
                'url_before', 
            ], 
            'm_cache_all_list' : [
                'info_vid', 
            ], 
            
            'm_first_cookie' : None, 
        }
        return out
    # end Var class

module_var = Var
# end var.py


