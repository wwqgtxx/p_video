# _call.py, p_video/lib/cache/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from .. import err, util
from ..var import var
from ..util import log, import_m_var

from ._dep import call_entry

def _init_module(module_name):
    var_class = import_m_var(module_name)
    var.mvar = var_class(var)
    # init module var done

def do_call_module(raw_data = None):
    _init_module(var.module)
    # DEBUG log
    log.d('call (module/entry) ' + str(var.module) + '/' + str(var.entry))
    # TODO ERROR process, maybe better
    try:
        out = call_entry(var.entry, raw_data, key='.main')
    except err.PVError:
        raise
    except Exception as e:
        log.e('call (module/entry) ' + str(var.module) + '/' + str(var.entry) + ' failed ')
        er = err.UnknowError('call_module_entry', var.module, var.entry, raw_data)
        raise er from e
    return out

# end _call.py


