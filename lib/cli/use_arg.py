# use_arg.py, p_video/lib/cli/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from .. import err, util
from ..util import log
from ..var import var


def set_features(arg_info):
    f = var.feature
    mp = f['_module_feature_prefix']
    
    def enable_disable_feature(to, value, info):
        ed = []
        for i in to:	# check module feature
            if not i.startswith(mp) and (not i in f):
                log.w('unknow global feature ' + i)
            if (i in f) and (f[i] == value):
                if i in ed:
                    log.w('already ' + info + ' feature ' + i)
                else:
                    log.i(info + ' by default, feature ' + i)
            # check disable value in enable
            if (value == False) and (i in arg_info['enable']):	# disable
                log.w('conflict: now disable feature with --enable ' + i)
            f[i] = value
            ed.append(i)
    if 'enable' in arg_info:	# enable features
        enable_disable_feature(arg_info['enable'], True, 'enabled')
    if 'disable' in arg_info:	# disable features
        enable_disable_feature(arg_info['disable'], False, 'disabled')
    if 'feature' in arg_info:	# --set
        set_json_feature(arg_info['feature'])

def set_json_feature(to):
    f = var.feature
    mp = f['_module_feature_prefix']
    
    for i in to:
        if not i.startswith(mp) and (not i in f):
            log.w('unknow global feature ' + i)
        # check to set or merge
        if (not i in f) or (not isinstance(to[i], dict)):
            f[i] = to[i]	# just set it
        else:	# merge dict
            f[i] = util.merge_dict_obj(f[i], to[i])


def use(arg_info):
    ai = arg_info
    # save raw cli arg_info
    var.raw_cli_config = util.json_clone(ai)
    
    # set data to var
    if '_debug' in ai:
        var.debug = ai['_debug']
    if 'module' in ai:
        var.module = ai['module']
    if 'entry' in ai:
        var.entry = ai['entry']
    if 'rest' in ai:
        var.rest = ai['rest']
    if 'raw_url' in ai:
        var.raw_url = ai['raw_url']
    # features
    set_features(ai)
    
    # set log
    f = var.feature
    if f['debug']:
        log.log_function = True
        log.log_module = True
        log.log_debug = True
    else:
        log.log_function = False
        log.log_debug = False
        
        log_level = f['log_level']
        if log_level == 'quiet':
            log.log_module = False
            log.quiet_mode = True
        else:	# normal mode
            log.quiet_mode = False


# end use_arg.py


