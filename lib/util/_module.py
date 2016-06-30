# _module.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

import importlib

from .. import err


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
        pass
    
    # TODO process module features
    # TODO process cache_use_list
    # end MVar class

# end _module.py


