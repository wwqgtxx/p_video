# info_vid.py, p_video/lib/m/e_271/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

import re

from ... import err, net, util
from ...util import log, MEntry

from . import var, _common


def _get_vid(html):
    re_list = var._RE_VID
    ignore_list = var._IGNORE_VID
    
    out = {}
    for key in re_list:
        try:
            one = re.findall(re_list[key], html)[0]
            out[key] = one
        except Exception as e:
            if key in ignore_list:
                log.w('ignore get_vid [' + key + ']')
                one = None
            else:
                log.e('can not get_vid [' + key + ']')
                er = err.ConfigError('get_vid', key)
                raise er from e
    return out


class Entry(MEntry):
    '''
    module/entry: m.e_271.info_vid
    
    data : {
        '_raw' : {
            'key' : '', 
            'raw_url' : '', 
        }, 
    }
    
    -> {
        'key' : '', 
        'url' : '', 	# raw_url
        'url_pure' : '', 
        
        'vid' : {
            'vid' : '', 
            'tvid' : '', 	# main vid
            'aid' : '', 	# albumID
            'flag_vv' : False, 
        }, 
    }
    '''
    # no dep
    
    def do_p(self, data):
        # load html_page
        raw_url = data['_raw']['raw_url']
        req = {
            'req' : [
                {
                    'url' : raw_url, 
                    'res_type' : 'text', 
                }, 
            ], 
        }
        html_text = net.http(req)['text']
        
        try:	# NOTE error process
            vid = _get_vid(html_text)
        except Exception as e:
            log.e('get vid_info failed from ' + raw_url)
            er = err.NotSupportURLError('get_vid', raw_url)
            raise er from e
        # make out data
        out = {
            'key' : data['_raw']['key'], 
            'url' : raw_url, 
            'url_pure' : _common.pure_url(raw_url), 
            'vid' : vid, 
        }
        return out
    # end Entry class

module_entry = Entry
# end info_vid.py


