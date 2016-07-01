# info_vms.py, p_video/lib/m/e_271/

import random
import uuid

from ... import err, util, net
from ...util import log, MEntry

from . import var, _common


def gen_auth_key(ugc_auth_key, tm, tvid):
    auth_key = util.hash_md5(util.hash_md5(ugc_auth_key) + str(tm) + str(tvid))
    return auth_key

# com.qiyi.player.core.model.remote.MixerRemote.getRequest()
def _raw_make_first_url(
        tvid, 
        vid, 
        tm, 	# NOTE should be set
        
        set_vinfo = True, 	# NOTE default value is True
        set_vv = False, 	# NOTE default value is False
        set_um = False, 	# NOTE default value is False
        
        ugc_auth_key = '', 	# NOTE can be null (can be set, the password)
        qyid = '', 	# TODO maybe empty or random
        puid = '', 	# NOTE can be empty
        thdk = '', 	# NOTE can be empty
        thdt = '', 	# NOTE can be empty
        set_locale_zh_tw = False):	# NOTE default value is False
    # _loc3 :uint = getTimer()
    auth_key = gen_auth_key(ugc_auth_key, tm, tvid)
    
    vinfo = 0
    vv = ''
    um = 0
    if set_vinfo:
        vinfo = 1
    if set_vv:
        vv = '&vv=821d3c731e374feaa629dcdaab7c394b'
    if set_um:
        um = 1
    
    out = '/vms?key=fvip&src=1702633101b340d8917a69cf8a4b8c7c&tvId=' + tvid + "&vid=" + vid
    out += '&vinfo=' + str(vinfo) + '&tm=' + str(tm)
    out += '&qyid=' + qyid + '&puid=' + puid
    out += '&authKey=' + auth_key + '&um=' + str(um) + vv
    out += '&pf=b6c13e26323c537d' + '&thdk=' + thdk + '&thdt=' + thdt
    out += '&rs=1' + '&k_tag=1' + '&qdv=1'
    if set_locale_zh_tw:
        out += '&locale=zh_tw'
    # _loc1 = Config.MIXER_VX_URL + _loc7 + '&vf=' + calc(_loc7, _loc7)
    return out

def _make_first_url(raw, vf):
    out = var._MIXER_VX_URL + raw + '&vf=' + vf
    return out


class Entry(MEntry):
    '''
    module/entry: m.e_271.info_vms
        just download (get) vms json info, not parse it
    
    data : {
        '_raw' : {
            'url' : '', 	# raw html page url
        }, 
    }
    
    -> {
        'info_vid' : {}, 
        'vms' : {}, 	# raw vms json (not parse it)
    }
    '''
    
    def _make_part_first_url(self, info_vid):
        tvid = info_vid['tvid']
        vid = info_vid['vid']
        # gen tm
        tm = random.randint(500, 5000)
        
        # get flags from module features
        f = self.gvar.feature
        set_um = f['m_set_um']
        set_vv = f['m_set_vv']
        auth_key = f['m_auth_key']
        set_locale_zh_tw = f['m_set_locale_zh_tw']
        
        # FIXME gen random qyid
        qyid = uuid.uuid4().hex
        
        out = _raw_make_first_url(tvid, vid, tm, qyid=qyid, set_vv=set_vv, set_um=set_um, ugc_auth_key=auth_key, set_locale_zh_tw=set_locale_zh_tw)
        return out
    
    def get_dep(self, gvar, data):
        dep = super().get_dep(gvar, data)
        
        self._key = _common.pure_url(data['_raw']['url'])
        # check get info_vid (first)
        if self._check_dep_key('info_vid', data):
            dep.append({
                'entry' : 'info_vid', 
                'key' : self._key, 
                'raw' : {
                    'raw_url' : data['_raw']['url'], 
                }, 
            })
            return dep
        # check get key_vf (never cache key_vf)
        if self._check_dep_key('key_vf', data):
            info_vid = self._get_key_data(self._key, data['info_vid'])['vid']
            self._part_first_url = self._make_part_first_url(info_vid)
            
            dep.append({
                'entry' : 'key_vf', 
                'key' : self._key, 
                'raw' : self._part_first_url, 
            })
            return dep
        return dep
    
    def do_p(self, data):
        # make first_url
        key_vf = self._get_key_data(self._key, data['key_vf'])
        first_url = _make_first_url(self._part_first_url, key_vf)
        
        log.i('first_url ' + first_url)
        # load vms json
        req = {
            'req' : [
                {
                    'url' : first_url, 
                    'res_type' : 'json', 
                }, 
            ], 
        }
        vms = net.http(req)['json']
        # check OK code
        if vms['code'] != var._CODE_OK['info_vms']:
            log.e('vms.code [' + vms['code'] + '] != ' + var._CODE_OK['info_vms'])
            er = err.MethodError('check_ok_code', 'vms.code', vms['code'], var._CODE_OK['info_vms'])
            raise er
        out = {
            'info_vid' : self._get_key_data(self._key, data['info_vid']), 
            'vms' : vms, 
        }
        return out
    # end Entry class

module_entry = Entry
# end info_vms.py


