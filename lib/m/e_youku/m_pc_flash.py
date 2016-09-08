# m_pc_flash.py, p_video/lib/m/e_youku/

from ... import err, util
from ...util import log, MEntry

from . import var, _common


class Entry(MEntry):
    '''
    module/entry: e_youku.m_pc_flash
        method: pc_flash
    
    method entry DEPendencies graph
    ```
    + m_pc_flash
        + url_file
            + url_before
                + info_first
                    - info_vid
    ```
    
    '''
    
    def get_dep(self, gvar, data):
        dep = super().get_dep(gvar, data)
        
        # TODO check input raw_url
        raw_url = gvar.raw_url[0]
        
        self._key = _common.pure_url(raw_url)
        # check url_file
        if self._check_dep_key('url_file', data):
            dep.append({
                'entry' : 'url_file', 
                'key' : self._key, 
                'raw' : {
                    'url' : raw_url, 
                }, 
            })
            return dep
        return dep
    
    def do_p(self, data):
        raw = self._get_key_data(self._key, data['url_file'])
        pvinfo = raw['pvinfo']
        info_vid = raw['info_vid']
        data = raw['first']['data']
        
        # gen pvinfo.info data
        i = {
            'url' : info_vid['url'], 
            'url_pure' : info_vid['url_pure'], 
            
            'title' : data['show']['title'], 
            'title_extra' : {
                'no' : int(data['show']['stage']), 	# FIXME maybe BUG here
                
                # TODO not support `sub`, `short` here
            }, 
            
            'site' : var.SITE, 
            'site_name' : var.SITE_NAME, 
            
            'vid' : info_vid['vid']['vid'], 
            'vid_extra' : info_vid['vid'], 
        }
        pvinfo['info'] = i
        # more process on pvinfo
        return util.make_pvinfo_output(pvinfo)
    # end Entry class

module_entry = Entry
# end m_pc_flash.py


