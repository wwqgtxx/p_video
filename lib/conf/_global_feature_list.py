# _global_feature_list.py, p_video/lib/conf/

def get_feature_init():
    out = {	# global features list and init (default) status (value)
        'debug' : False, 
        
        'log_level' : '', 	# in ['' (normal), 'quiet']
        
        # parse config
        'fast_parse' : False, 
        'fix_size' : True, 
        
        # cache config
        'cache_all' : False, 		# cache all items by default (used for auto-conf)
        'cache_nothing' : False, 	# not cache is first than cache
        
        'cache_blacklist' : [], 	# should be set by init of module.var
        
        'cache_use' : [], 	# use input `pvinfo._cache`
        'cache_not' : [], 	# not use cache item from input
        'cache_out' : [], 	# output cache items
        
        '_cache_use_list' : [], # final processed cache items to use list
        
        # select parse
        'hd' : [None, None], 	# [hd_min, hd_max] select video by hd
        'i' : [None, None], 	# [i_min, i_max] select part file by index
        
        # net.http() default config
        'http_req_default' : {
            'pool_size' : 16, 
            'timeout_s' : 10, 
            
            'retry' : 3, 
            'retry_wait_s' : 1, 
        }, 
        
        # handwich_bridge config
        'handwich_bridge_server' : {
            'ip' : '127.0.0.1', 
            'port' : 48271, 
            'key' : '', 
        }, 
        
        # TODO
        
        # TODO maybe should not in features here
        '_module_feature_prefix' : 'm_', 
    }
    return out

# end _global_feature_list.py


