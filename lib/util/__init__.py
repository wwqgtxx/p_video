# __init__.py, p_video/lib/util/
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

from ._module import MVar, import_m_var, import_m_entry
from ._m_entry import MEntry

from ._log import Log, log

from ._common import (
    hash_md5, 
    
    json_clone, 
    json_cmp, 
    json_print, 
    
    merge_dict_obj, 
)


# end __init__.py


