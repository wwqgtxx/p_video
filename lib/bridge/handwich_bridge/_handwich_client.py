# _handwich_client.py, p_video/lib/bridge/handwich_bridge/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

import json
import urllib.parse

from ... import err, net
from ...util import log


class HandwichHost(object):
    # TODO support load_core
    
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 48271
        self.core_id = 'cmd5'
        self.key = None
    
    def _make_base_url(self):
        out = 'http://' + str(self.ip) + ':' + str(self.port) + '/handwich_bridge/'
        return out
    
    def _make_version_url(self):
        out = self._make_base_url() + 'version'
        if self.key != None:
            out += '?key=' + str(self.key)
        return out
    
    def _make_call_core_url(self, f, a=None):
        out = self._make_base_url() + 'call?core=' + str(self.core_id)
        if self.key != None:
            out += '&key=' + str(self.key)
        out += '&f=' + str(f)
        if a != None:
            out += '&a=' + urllib.parse.quote(json.dumps(a))
        return out
    
    def _req(self, url, res_type):
        req = {
            'req' : [
                {
                    'url' : url, 
                    'res_type' : res_type, 
                }, 
            ], 
        }
        log.d('handwich_bridge --> ' + url)
        out = net.http(req)[res_type]
        return out
    
    # get handwich_bridge version
    def get_version(self):
        return self._req(self._make_version_url(), 'text')
    
    # call handwich_bridge core
    def call_core(self, f, a=None):
        return self._req(self._make_call_core_url(f, a=a), 'json')
    # end HandwichHost class


# end _handwich_client.py


