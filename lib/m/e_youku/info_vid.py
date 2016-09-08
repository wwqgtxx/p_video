# info_vid.py, p_video/lib/m/e_youku/

import re

from ... import err, util, net
from ...util import log, MEntry

from . import var, _common


def _get_vid(html):
    re_list = var._RE_VID
    out = {}
    for key in re_list:
        out[key] = re.findall(re_list[key], html)[0]
    return out


class Entry(MEntry):
    '''
    module/entry: m.e_youku.info_vid
    
    data : {
        '_raw' : {
            'url' : '', 	# raw html page url
        }, 
    }
    
    -> {
        'key' : '', 
        'url' : '', 	# raw_url
        'url_pure' : '', 
        
        'vid' : {
            'vid' : '', 	# main vid
        }, 
    }
    '''
    # no dep
    
    def do_p(self, data):
        # load html page
        raw_url = data['_raw']['url']
        req = {
            'req' : [
                {
                    'url' : raw_url, 
                    'res_type' : 'text', 
                }, 
            ], 
        }
        html_text = net.http(req)['text']
        
        try:
            vid = _get_vid(html_text)
        except Exception as e:
            log.e('get vid_info failed from ' + raw_url)
            er = err.NotSupportURLError('get_vid', raw_url)
            raise er from e
        out = {
            'key' : _common.pure_url(raw_url), 
            'url' : raw_url, 
            'url_pure' : _common.pure_url(raw_url), 
            'vid' : vid, 
        }
        return out
    # end Entry class

module_entry = Entry
# end info_vid.py


