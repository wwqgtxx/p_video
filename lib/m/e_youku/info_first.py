# info_first.py, p_video/lib/m/e_youku/

import time

from ... import err, util, net
from ...util import log, MEntry

from . import var, _common


def _make_first_url(vid):
    out = var._GET_JSON + '?vid=' + vid + '&ct=10'
    out += '&time=' + str(int(time.time() * 1e3))
    return out


class Entry(MEntry):
    '''
    module/entry: m.e_youku.info_first
    
    data : {
        '_raw' : {
            'url' : '', 	# raw html page url
        }, 
    }
    
    -> {
        'info_vid' : {}, 
        'first_raw' : '', 	# raw format (text)
        'first' : {}, 	# after parse json text
    }
    '''
    
    def _get_first_url(self, info_vid):
        vid = info_vid['vid']['vid']
        return _make_first_url(vid)
    
    def get_dep(self, gvar, data):
        dep = super().get_dep(gvar, data)
        
        self._key = _common.pure_url(data['_raw']['url'])
        # check get info_vid
        if self._check_dep_key('info_vid', data):
            dep.append({
                'entry' : 'info_vid', 
                'key' : self._key, 
                'raw' : data['_raw'], 
            })
            return dep
        return dep
    
    def do_p(self, data):
        info_vid = self._get_key_data(self._key, data['info_vid'])
        first_url = self._get_first_url(info_vid)
        
        log.i('first_url ' + first_url)
        # load it
        # TODO support first cookie
        req = {
           'req' : [
               {
                   'url' : first_url, 
                   'res_type' : 'json', 
               }, 
           ], 
        }
        raw = net.http(req)
        # TODO check OK code
        
        out = {
            'info_vid' : info_vid, 
            'first_raw' : raw['text'], 
            'first' : raw['json'], 
        }
        return out
    # end Entry class

module_entry = Entry
# end info_first.py


