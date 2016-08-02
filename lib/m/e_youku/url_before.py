# url_before.py, p_video/lib/m/e_youku/

from ...util import MEntry

from . import var, _common, _bridge


def _make_one_url(raw):
    out = var._GET_FLV_PATH + raw + '&yxon=1&special=true'
    return out


class Entry(MEntry):
    '''
    module/entry: m.e_youku.url_before
    
    data : {
        '_raw' : {
            'url' : '', 	# raw html page url
        }, 
    }
    
    -> {
        'info_vid' : {}, 
        'first' : {}, 	# info_first
        'pvinfo' : {	# raw pvinfo
            'video' : [], 
        }, 
    }
    '''
    
    def get_dep(self, gvar, data):
        dep = super().get_dep(gvar, data)
        
        self._key = _common.pure_url(data['_raw']['url'])
        # check info_first
        if self._check_dep_key('info_first', data):
            dep.append({
                'entry' : 'info_first', 
                'key' : self._key, 
                'raw' : data['_raw'], 
            })
            return dep
        return dep
    
    def do_p(self, data):
        info_first = self._get_key_data(self._key, data['info_first'])
        
        # get raw url_before with handwich_bridge/doll_youku
        first_raw = info_first['first_raw']
        first = info_first['first']
        # make filetype_list
        to_do = []
        for i in first['data']['stream']:
            stream_type = i['stream_type']
            to_do.append(var._TO_FILETYPE[stream_type])
        # init bridge
        _bridge.init(self.gvar)
        raw = _bridge.parse(first_raw, to_do)
        
        # build raw pvinfo
        pvinfo = {
            'video' : [], 
        }
        
        for s in first['data']['stream']:
            stream_type = s['stream_type']
            
            v = {}
            v['hd'] = var._TO_HD[stream_type]
            v['size_px'] = [
                int(s['width']), 
                int(s['height']), 
            ]
            # NOTE format here should be `flv`
            v['format'] = 'flv'
            
            raw_list = raw[var._TO_FILETYPE[stream_type]]
            v['file'] = []	# file list
            for i in range(len(s['segs'])):
                seg = s['segs'][i]
                
                f = {}
                f['size_byte'] = int(seg['size'])
                f['time_s'] = int(seg['total_milliseconds_video']) / 1e3
                
                f['url'] = _make_one_url(raw_list[i])
                v['file'].append(f)
            pvinfo['video'].append(v)
        # sort video by hd
        pvinfo['video'].sort(key = lambda x: x['hd'], reverse=True)
        out = {
            'info_vid' : info_first['info_vid'], 
            'first' : first, 
            'pvinfo' : pvinfo, 
        }
        return out
    # end Entry class

module_entry = Entry
# end url_before.py


