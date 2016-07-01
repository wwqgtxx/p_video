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


# TODO


# end _pvinfo_pretty_print.py


