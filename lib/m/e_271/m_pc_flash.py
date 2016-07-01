# m_pc_flash.py, p_video/lib/m/e_271/
#
#    p_video : parse to get video info from some web sites. 
#    Copyright (C) 2016 sceext <sceext@foxmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>. 
#

from ... import err, util
from ...util import log, MEntry

from . import var, _common


class Entry(MEntry):
    '''
    module/entry: e_271.m_pc_flash
        method: pc_flash
    
    
    method entry DEPendencies graph
    ```
    + m_pc_flash
        + url_file
            + url_before
                + info_vms
                    - info_vid
                    - key_vf
                - vv_key (optional)
    ```
    
    '''
    
    def get_dep(self, gvar, data):
        dep = super().get_dep(gvar, data)
        # TODO maybe support just imput vid info
        
        # check input raw_url
        length = len(gvar.raw_url)
        if length < 1:
            log.e('no input URL')
            raise err.ConfigError('gvar.raw_url', gvar.raw_url)
        elif length > 1:
            log.w('only use first input URL')
        raw_url = gvar.raw_url[0]
        
        # TODO check input url (support re)
        
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
        vi = raw['vms']['data']['vi']
        
        # gen pvinfo.info data
        i = {
            'url' : info_vid['url'], 
            'url_pure' : info_vid['url_pure'], 
            
            'title' : vi['vn'], 
            'title_extra' : {
                'sub' : vi['subt'], 
                
                # FIXME `no` maybe BUG here
                'no' : vi['pd'], 
                'short' : vi['an'], 
            }, 
            
            'site' : var.SITE, 
            'site_name' : var.SITE_NAME, 
            
            'vid' : info_vid['vid']['tvid'], 	# here choose `tvid` as the main vid
            'vid_extra' : info_vid['vid'], 
        }
        pvinfo['info'] = i
        # more process on pvinfo
        return util.make_pvinfo_output(pvinfo)
    # end Entry class

module_entry = Entry	# exports
# end m_pc_flash.py


