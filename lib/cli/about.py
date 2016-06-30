# about.py, p_video/lib/cli/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from .. import version


def get_version_info():	# --version
    raw = '''

    p_video  Copyright (C) 2016  sceext <sceext@foxmail.com>
    This program comes with ABSOLUTELY NO WARRANTY. This is free software, and 
    you are welcome to redistribute it under certain conditions. 

License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>. 
Please use "--license" or read LICENSE for more details. \
'''
    out = version.version_str + raw
    return out

def get_license():	# --license
    out = '''\
    p_video : parse to get video info from some web sites. 
    Copyright (C) 2016 sceext <sceext@foxmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>. \
'''
    return out


# end about.py


