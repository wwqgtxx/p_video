# url_before.py, p_video/lib/m/e_271/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from ...util import MEntry

from . import var, _common


class Entry(MEntry):
    '''
    module/entry: m.e_271.url_before
        make before (final) file URLs
    
    data : {
        '_raw' : {
            'url' : '', 	# raw html page url
        }, 
    }
    
    -> {
        'info_vid' : {}, 
        'vms' : {}, 	# raw vms json info
        'pvinfo' : {	# raw pvinfo
            'video' : [], 
        }, 
    }
    '''
    
    def get_dep(self, gvar, data):
        dep = super().get_dep(gvar, data)
        
        self._key = _common.pure_url(data['_raw']['url'])
        # check info_vms
        if self._check_dep_key('info_vms', data):
            dep.append({
                'entry' : 'info_vms', 
                'key' : self._key, 
                'raw' : {
                    'url' : data['_raw']['url'], 
                }, 
            })
            return dep
        # TODO check vv_key
        return dep
    
    def do_p(self, data):
        info_vms = self._get_key_data(self._key, data['info_vms'])
        vms = info_vms['vms']
        pvinfo = {
            'video' : [], 
        }
        
        def get_px(raw):
            try:
                out = raw.split('x')
                out = [int(out[0]), int(out[1])]
            except Exception:	# ignore Error
                out = [-1, -1]
            return out
        
        def get_checksum(raw):
            checksum = raw.split('?', 1)[0].rsplit('/', 1)[1].rsplit('.', 1)[0]
            out = {
                'md5' : checksum, 
            }
            return out
        
        def make_before_url(du, raw):
            # FIXME maybe BUG here
            return du + raw
        
        # parse vms to get each video quality item
        vp = vms['data']['vp']
        du = vp['du']
        for vs in vp['tkl'][0]['vs']:
            v = {}
            v['hd'] = var._TO_HD[int(vs['bid'])]
            v['size_px'] = get_px(vs['scrsz'])
            # NOTE format here should be `flv`
            v['format'] = 'flv'
            
            v['file'] = []	# file list
            for fs in vs['fs']:
                f = {}
                f['size_byte'] = int(fs['b'])
                f['time_s'] = int(fs['d']) / 1e3
                f['checksum'] = get_checksum(fs['l'])
                
                f['url'] = make_before_url(du, fs['l'])
                v['file'].append(f)
            pvinfo['video'].append(v)
        # sort video by hd
        pvinfo['video'].sort(key = lambda x: x['hd'], reverse=True)
        out = {
            'info_vid' : info_vms['info_vid'], 
            'vms' : vms, 
            'pvinfo' : pvinfo, 
        }
        return out
    # end Entry class

module_entry = Entry
# end url_before.py


