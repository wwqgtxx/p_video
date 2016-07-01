# _pvinfo_pretty_print.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 
'''

pvinfo (json) format
```
{
    '#' : 'p_video/pvinfo struct', 	# format self-comment
    'mark_uuid' : 'fa8b4922-983f-4bca-8127-9028055fad89', 	# uuid mark
    'port_version' : '0.8.0-1', 	# version of p_video/pvinfo struct format
    
    'config' : {	# CLI or inner config info (config output/input) (with --set-json)
        'info_source' : '', 	# p_video version info
        
        'module' : '', 	# used module (module name)
        'entry' : '', 	# module first (root) entry (name)
        
        'rest' : [], 	# [optional] rest command line arguments
        'raw_url' : [], # [optional]
        
        'enable' : [], 	# [optional] enabled features (only by CLI, not include defaults)
        'disable' : [], # [optional] disabled features (only by CLI, not include defaults)
        
        'feature' : {}, # [optional] set features
        
        'comment' : [], # [optional] --comment
    }, 
    
    'info' : {
        'url' : '', 		# raw input url
        'url_pure' : '', 	# pured url
        
        'title' : '', 	# main video title
        'title_extra' : {	[optional]
            'sub' : '', 
            'no' : -1, 
            'short' : '', 
        }, 
        
        'site' : '', 
        'site_name' : '', 
        
        'vid' : '', 	# main vid (if possible)
        'vid_extra' : {}, 	# [optional] more vid info (if possible)
    }, 
    
    'video' : [		# multi-video formats (quality)
        {
            'hd' : 0, 
            'quality' : '', 
            
            'size_px' : [-1, -1], 	# video px [x, y]
            'size_byte' : -1, 
            'time_s' : -1, 
            
            'format' : '', 	# in ['mp4', 'flv', 'm3u8', 'm3u8/ts']
            # TODO support video-only, audio-only formats
            
            'count' : 0, 
            'file' : [
                {
                    'type' : ['http'], 	# [optional] download protocol/method
                    
                    'size_byte' : -1, 	# file size in Byte
                    'time_s' : -1, 	# video time in Second
                    
                    'url' : '', 	# or [] for multi-URLs
                    'header' : {}, 	# [optional]
                    
                    'checksum' : {	# [optional]
                        'md5' : '', 
                    }, 
                    'expire' : '', 	# [optional]
                }, 
            ], 
        }, 
    ]
    
    
    '_raw' : {}, 	# [optional] input for module/entry _raw (json) data
    '_cache' : {}, 	# [optional] input/output cache (json) data
    
    'last_update' : '', 	# last update time, ISO-Z
}
```

'''

from collections import OrderedDict

from ._common import json_clone, gen_last_update


def _restruct_key(old, key_list=[], rest_sort_reverse=False):
    '''
    restruct a dict to OrderedDict
    order is in key_list
    
    rest keys is keys in old but not in key_list
    rest keys is sort by rest_sort_reverse
    if rest_sort_reverse == None, rest keys will not be sort
    '''
    raw = old.copy()	# not modify old dict
    out = OrderedDict()
    for key in key_list:
        if key in raw:	# ignore not exist keys
            out[key] = raw.pop(key)
    # get rest key list and sort keys by key name
    rest_key = [i for i in raw]
    if rest_sort_reverse != None:
        rest_key.sort(reverse=rest_sort_reverse)
    # add rest keys
    for key in rest_key:
        out[key] = raw.pop(key)
    return out


def pvinfo_pretty_print(pvinfo):
    # key order list
    pvinfo_list = [	# pvinfo
        '#', 
        'mark_uuid', 
        'port_version', 
        'config', 
        'info', 
        'video', 
        '_raw', 
        '_cache', 
        'last_update', 
    ]
    config_list = [	# pvinfo.config
        'info_source', 
        'module', 
        'entry', 
        'rest', 
        'raw_url', 
        'enable', 
        'disable', 
        'feature', 
        'comment', 
    ]
    info_list = [	# pvinfo.info
        'url', 
        'url_pure', 
        'title', 
        'title_extra', 
        'site', 
        'site_name', 
        'vid', 
        'vid_extra', 
    ]
    title_extra_list = [	# pvinfo.info.title_extra
        'sub', 
        'no', 
        'short', 
    ]
    video_list = [	# pvinfo.video[]
        'hd', 
        'quality', 
        'size_px', 
        'size_byte', 
        'time_s', 
        'format', 
        'count', 
        'file', 
    ]
    file_list = [	# pvinfo.video[].file[]
        'type', 
        'size_byte', 
        'time_s', 
        'url', 
        'header', 
        'checksum', 
        'expire', 
    ]
    # restruct pvinfo
    pvinfo = _restruct_key(json_clone(pvinfo), pvinfo_list)
    if 'config' in pvinfo:
        pvinfo['config'] = _restruct_key(pvinfo['config'], config_list)
    pvinfo['info'] = _restruct_key(pvinfo['info'], info_list)
    if 'title_extra' in pvinfo['info']:
        pvinfo['info']['title_extra'] = _restruct_key(pvinfo['info']['title_extra'], title_extra_list)
    for i in range(len(pvinfo['video'])):
        pvinfo['video'][i] = _restruct_key(pvinfo['video'][i], video_list)
        v = pvinfo['video'][i]
        for j in range(len(v['file'])):
            v['file'][j] = _restruct_key(v['file'][j], file_list)
            #f = v['file'][j]
    # TODO sort (key of) sub items, such as header, checksum
    
    # sort video by hd
    pvinfo['video'].sort(key = lambda x: x['hd'], reverse=True)
    # reset last_update
    pvinfo['last_update'] = gen_last_update()
    
    return pvinfo

# end _pvinfo_pretty_print.py


