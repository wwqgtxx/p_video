# _module.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

import importlib

from .. import err
from ._log import log
from ._common import merge_dict_obj


def _import_module(name):
    to = '.' + name
    try:
        out = importlib.import_module(to, __name__)
    except Exception as e:
        log.e('can not import ' + name)
        er = err.ConfigError('import', name, to)
        raise er from e
    return out

def import_m_var(module_name):
    name = '..m.' + module_name + '.var'
    m = _import_module(name)
    return m.module_var

def import_m_entry(module_name, entry_name):
    # NOTE do not process entry class cache
    name = '..m.' + module_name + '.' + entry_name
    m = _import_module(name)
    return m.module_entry


class MVar(object):
    
    def __init__(self, gvar):
        self.gvar = gvar
        
        self._init_module_features()
        
        self._init_cache_config()
        self._clean_cache()
        
        # MVar common init done
        self._init()	# subclass init
    # init function for subclass
    def _init(self):
        pass
    @staticmethod
    def get_module_feature_init():
        out = {
            'm_cache_blacklist' : [], 
            'm_cache_all_list' : [], 
        }
        return out
    
    # common init function
    def _init_module_features(self):
        f = self.gvar.feature
        mp = f['_module_feature_prefix']
        mf = self.get_module_feature_init()
        # set (default) or update or merge feature value
        for i in mf:
            if not i in f:
                f[i] = mf[i]	# set default value
            elif isinstance(mf[i], dict):	# merge dict
                f[i] = merge_dict_obj(mf[i], f[i])
            # else: just update value (override) (ignore)
        # WARNING unknow module features
        for i in f:
            if i.startswith(mp) and (not i in mf):
                log.w('unknow module feature ' + i)
    
    def _init_cache_config(self):
        f = self.gvar.feature
        use = {}
        out = {i :True for i in f['cache_out']}
        # check `cache_all`
        if f['cache_all']:
            for i in f['m_cache_all_list']:
                use[i] = True
                # auto set cache_out
                out[i] = True
        # check `cache_use`
        for i in f['cache_use']:
            use[i] = True
            # NOTE will not auto-set cache_out here
        # NOTE not_cache is first than cache
        # check `cache_not`
        for i in f['cache_not']:
            if i in use:
                use.pop(i)
            # auto remove cache_out
            if i in out:
                out.pop(i)
        # check `cache_nothing`
        if f['cache_nothing']:
            # clear all cache config
            use = {}
            out = {}
        # check cache_blacklist
        for i in f['m_cache_blacklist']:
            if i in use:
                use.pop(i)
            if i in out:
                out.pop(i)
        # done, set f._cache_use_list, cache_out
        to = [i for i in use]
        # DEBUG log
        log.d('_cache_use_list = ' + str(to))
        f['_cache_use_list'] = to
        f['cache_out'] = [i for i in out]
    
    def _clean_cache(self):
        # clean each item not in gvar.cache, to actually prevent use cache
        f = self.gvar.feature
        for i in self.gvar.cache:
            if not i in f['_cache_use_list']:
                self.gvar.cache.pop(i)
    # end MVar class

# end _module.py


