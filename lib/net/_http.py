# _http.py, p_video/lib/net/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 
'''
p_video global http request method

data in net.http(data)  (json format)
    
    {
        'pool_size' : 16, 	# [ optional ]
        'timeout_s' : 10, 	# [ optional ]
        'retry' : 3, 		# [ optional ]
        'retry_wait_s' : 1, 	# [ optional ]
        'raise_error' : True, 	# [ optional ]
        
        'req_with' : 'curl', 	# [ optional ] in ['curl', 'native' (python3.5)]
        
        'req' : [	# http request list
            {
                'url' : '', 
                'method' : 'GET', 	# [ optional ]
                'header' : None, 	# [ optional ] overwrite default headers
                'header_extra' : {}, 	# [ optional ] add extra headers
                
                # data to POST
                'data' : None, 		# [ optional ]
                'data_type' : 'blob', 	# [ optional ] POST data_type, in ['blob', 'text', 'json', 'form' (www-form-urlencoded)]
                
                # res type, auto-convert, error process
                'res_type' : 'json', 	# in ['blob', 'text', 'json', 'xml']
                'encoding' : 'utf-8', 	# [ optional ] text encoding
            }, 
        ], 
        'ret_single' : True, 	# [ optional ] not return [] with len(req) == 1
    }
    
    
    net.http() return (json) format
    
    [
        {
            'error' : [], 	# [ optional ] error object (Exception), include each retry
            
            # data formats
            'blob' : None, 
            'text' : None, 
            'json' : None, 
            'xml' : None, 
        }, 
    ]
    
    TODO pool request many times, and merge success results
    TODO Ctrl+C (SIGINT) reset (retry) network request

'''

import json
import xml.etree.ElementTree as ET

import subprocess
import multiprocessing.dummy as multiprocessing
import urllib.request

from .. import err
from ..var import var
from ..util import log


def _req_with_native(data, i):
    
    # TODO
    pass

def _req_with_curl(data, i):
    
    # TODO
    pass

def _map_do(data):
    
    # TODO
    pass

def _encode_post_data(data):
    
    # TODO
    pass

def _decode_res_data(data):
    
    # TODO
    pass


def http(data):
    
    # TODO
    pass


# end _http.py


