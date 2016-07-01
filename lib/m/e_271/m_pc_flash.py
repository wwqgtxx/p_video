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

from ...util import MEntry

from . import var, _common


class Entry(MEntry):
    '''
    module/entry: e_271.m_pc_flash: method: pc_flash
    
    
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
        super().get_dep(gvar, data)
        
        # TODO
    
    def do_p(data):
        
        # TODO
        pass
    # end Entry class

module_entry = Entry	# exports
# end m_pc_flash.py


