# url_file.py, p_video/lib/m/e_youku/

from ... import err, util, net
from ...util import MEntry

from . import var, _common


class Entry(MEntry):
    '''
    module/entry: m.e_youku.url_file
    
    data : {
        '_raw' : {
            'url' : '', 	# raw html page url
        }, 
    }
    
    -> {
        'info_vid' : {}, 
        'first' : {}, 
        'pvinfo' : {}, 	# raw pvinfo
    }
    '''
    
    def get_dep(self, gvar, data):
        dep = super().get_dep(gvar, data)
        
        self._key = _common.pure_url(data['_raw']['url'])
        # check url_before
        if self._check_dep_key('url_before', data):
            dep.append({
                'entry' : 'url_before', 
                'key' : self._key, 
                'raw' : data['_raw'], 
            })
            return dep
        return dep
    
    def do_p(self, data):
        out = self._get_key_data(self._key, data['url_before'])
        pvinfo = out['pvinfo']
        # count video and select hd i
        pvinfo = util.select_hd_i(util.count_video(pvinfo))
        
        def check_skip_file(f):
            if (not 'url' in f) or (f['url'] in ['', None]):
                return True
            return False
        # make http req to do list
        req = {
            'req' : [], 
            'ret_single' : False, 
        }
        for v in pvinfo['video']:
            for f in v['file']:
                if check_skip_file(f):
                    continue
                one = {
                    'url' : f['url'], 
                    'res_type' : 'json', 
                }
                req['req'].append(one)
        # TODO better process
        result = net.http(req)
        # TODO check OK code
        # get real final url from raw res info
        res = [i['json'][0]['server'] for i in result]
        # save results
        for v in pvinfo['video']:
            for f in v['file']:
                if not check_skip_file(f):
                    f['url'], res = res[0], res[1:]
        out['pvinfo'] = pvinfo
        return out
    # end Entry class

module_entry = Entry
# end url_file.py


