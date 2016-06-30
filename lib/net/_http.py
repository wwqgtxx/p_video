# _http.py, p_video/lib/net/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 
'''
p_video global http request method

req in net.http(req)  (json format)
    
    {
        'pool_size' : 16, 	# [ optional ]
        'timeout_s' : 10, 	# [ optional ]
        'retry' : 1, 		# [ optional ]
        'retry_wait_s' : 1, 	# [ optional ]
        'raise_error' : True, 	# [ optional ]
        
        'req_with' : 'curl', 	# [ optional ] in ['curl', 'native' (python3.5)]
        
        'req' : [	# http request list
            {
                'url' : '', 
                'method' : 'GET', 	# [ optional ]
                'header' : None, 	# [ optional ] overwrite default headers
                'header_extra' : {}, 	# [ optional ] add extra headers
                
                'use_compress' : True, 
                
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
import time

import subprocess
import multiprocessing.dummy as multiprocessing
import urllib.request

from .. import err, util
from ..var import var
from ..util import log

# TODO support global proxy config


def _req_with_native():
    # TODO
    pass

def _req_with_curl(url, timeout_s=None, header={}, method='GET', bin_curl='curl', use_compress=True):
    # TODO support POST data
    # TODO support other method (not only GET)
    
    # make curl arguments
    to = [bin_curl, url]
    to += ['-s', '-S']	# set log output
    to += ['--max-time', str(timeout_s)]
    if use_compress:
        to += ['--compressed']
    # gen headers
    for i in header:
        one = str(i) + ': ' + str(header[i])
        to += ['--header', one]
    # log curl CLI arguments
    log.d(' curl --> ' + str(to))
    # run curl and check exit_code
    PIPE = subprocess.PIPE
    result = subprocess.run(to, stdout=PIPE, check=True)
    # TODO maybe use timeout= for subprocess.run() here
    out = result.stdout
    return out

def _do_one_req(one, req):
    # get arg
    timeout = req['timeout_s']
    req_with = req['req_with']
    
    url = one['url']
    method = one['method']
    header = one['_header']
    use_compress = one['use_compress']
    # TODO support POST data
    # TODO support req with native
    out = {}
    # check req_with
    if req_with == 'curl':
        # TODO error process
        # TODO support get error info from curl
        blob = _req_with_curl(url, timeout_s=timeout, header=header, method=method, bin_curl=req['bin_curl'], use_compress=use_compress)
        # TODO log
        out['blob'] = blob
    else:
        log.e('not support net.http request with ' + req_with)
        raise err.ConfigError('http_req_with', req_with)
    return out

def _decode_res_data(blob, one, out):
    out['blob'] = blob
    
    res_type = one['res_type']
    if res_type in ['text', 'json', 'xml']:
        # TODO error process
        out['text'] = out['blob'].decode(one['encoding'])
    if res_type == 'json':
        # TODO process decoding (parse) error
        out['json'] = json.loads(out['text'])
    elif res_type == 'xml':
        # TODO process decoding (parse) error
        out['xml'] = ET.fromstring(out['text'])
    return out	# done

def _req_one_worker(raw):
    req, i = raw
    one = req['req'][i]
    
    out = {}
    out['error'] = []
    
    # TODO process retry and wait
    retry = req['retry']
    retry_wait = req['retry_wait_s']
    
    retry_count = -1
    blob = None
    while retry_count < retry:
        retry_count += 1
        # TODO log
        try:
            info = _do_one_req(one, req)
            blob = info['blob']
            break
        except Exception as e:
            out['error'].append(e)
            # TODO log error
        time.sleep(retry_wait)	# retry_wait
    # check retry success
    if blob == None:
        return out
    # TODO add log here
    try:
        out = _decode_res_data(blob, one, out)
    except Exception as e:
        out['error'].append(e)
        # TODO log error
    return out

def _map_do(req):
    to_do = []
    for i in range(len(req['req'])):
        one = [req, i]
        to_do.append(one)
    # TODO log map_do
    
    # use pool (thread)
    pool_size = req['pool_size']
    pool = multiprocessing.Pool(processes=pool_size)
    result = pool.map(_req_one_worker, to_do)
    pool.close()
    pool.join()
    return result


def _encode_post_data(req):
    # TODO
    return req

def http(req):
    # add default config
    req_default = {
        'pool_size' : 16, 
        'timeout_s' : 10, 
        'retry' : 1, 
        'retry_wait_s' : 1, 
        'raise_error' : True, 
        'req_with' : 'curl', 
        'bin_curl' : 'curl', 
        'ret_single' : True, 
    }
    req = util.merge_dict_obj(var.feature['http_req_default'], req)
    req = util.merge_dict_obj(util.json_clone(req_default), req)
    
    # merge one item default config
    one_default = {
        'method' : 'GET', 
        'use_compress' : True, 
        # POST
        'data' : None, 
        'data_type' : 'blob', 
        # res
        'res_type' : 'json', 
        'encoding' : 'utf-8', 
    }
    for i in range(len(req['req'])):
        req['req'][i] = util.merge_dict_obj(util.json_clone(one_default), req['req'][i])
        req['req'][i]['i'] = i	# set index to item
    # set default-header and merge headers
    default_header = var.feature['http_req_default']['default_header']
    for i in req['req']:
        if (not 'header' in i) or (i['header'] == None):
            i['header'] = util.json_clone(default_header)
        extra_header = i.get('extra_header', {})
        i['_header'] = util.merge_dict_obj(i['header'], extra_header)
    # TODO support POST data
    req = _encode_post_data(req)
    
    result = _map_do(req)
    
    # check raise error
    if req['raise_error']:
        for i in result:	# FIXME TODO now just raise first Error object, maybe can be improved
            if len(i['error']) > 0:
                e = i['error'][0]
                er = err.NetworkError('http_request', i, result, req)
                # TODO log error
                raise er from e
    # clean output result
    for i in result:
        if len(i['error']) < 1:
            i.pop('error')
    # check ret_single
    if req['ret_single'] and (len(result) == 1):
        return result[0]
    return result


# end _http.py


