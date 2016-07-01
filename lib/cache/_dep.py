# _dep.py, p_video/lib/cache/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from .. import err, util
from ..var import var
from ..util import log, import_m_entry


def _get_entry_obj(entry_name):
    if not entry_name in var.e:
        var.e[entry_name] = import_m_entry(var.module, entry_name)
    entry_class = var.e[entry_name]
    return entry_class()

def _gen_dep(dep):
    for i in dep:	# gen each dep
        entry = i['entry']
        raw = None
        key = None
        if 'raw' in i:
            raw = i['raw']
        if 'key' in i:
            key = i['key']
        # check use cache
        if entry in var.cache:
            c = var.cache[entry]
            data_in_cache = False
            for i in c:
                if util.json_cmp(i['key'], key):
                    data_in_cache = True
                    break
            if data_in_cache:
                log.i('use cache: entry ' + entry + ', key = ' + str(key))
                continue	# ignore this dep
        else:
            var.cache[entry] = []	# init cache data
        # gen data
        result = call_entry(entry, raw, key=key)
        # put in cache
        item = {
            'key' : key, 
            'ret' : result, 
        }
        var.cache[entry].append(item)
    # end _gen_dep


def call_entry(entry_name, raw, key=''):
    e = _get_entry_obj(entry_name)
    
    def make_data():
        data = util.json_clone(var.cache)
        data['_raw'] = raw
        return data
    
    # gen all dep data
    while True:
        dep = e.get_dep(var, make_data())
        if len(dep) < 1:
            break
        _gen_dep(dep)
    
    # INFO log
    log.i('call entry ' + entry_name + ', key = ' + str(key))
    
    # do_p
    try:	# FIXME ERROR process maybe improved
        result = e.do_p(make_data())
    except err.PVError:
        raise
    except Exception as e:
        log.e('entry.do_p() failed, entry ' + entry_name + ', key = ' + str(key))
        er = err.MethodError('entry.do_p', entry_name, key, raw)
        raise er from e
    return result


# end _dep.py


