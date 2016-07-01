# _make_pvinfo_output.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from .. import err, version
from ..var import var, PVINFO_MARK_UUID, PVINFO_PORT_VERSION

from ._hd_quality import get_quality
from ._common import json_clone, gen_last_update
from ._pvinfo_pretty_print import pvinfo_pretty_print


def _make_config():
    raw = var.raw_cli_config
    out = {
        'info_source' : version.version_str, 
        
        'module' : var.module, 
        'entry' : var.entry, 
        
        'rest' : var.rest, 
        'raw_url' : var.raw_url, 
        
        'enable' : raw['enable'], 
        'disable' : raw['disable'], 
        
        'feature' : raw['feature'], 
        
        # TODO maybe support merge-comment (from CLI and stdin/json pvinfo.config)
        'comment' : raw['comment'], 
    }
    return out

def _make_cache():
    out = {}
    for i in var.feature['cache_out']:
        if i in var.cache:
            out[i] = var.cache[i]
    return out

def _add_quality(pvinfo, keep_raw_quality=True, join_raw_quality='-'):
    for v in pvinfo['video']:
        quality = get_quality(v['hd'])
        if (not 'quality' in v) or (not keep_raw_quality):
            v['quality'] = quality
        else:
            v['quality'] = quality + join_raw_quality + v['quality']
    return pvinfo

def _clean_pvinfo(pvinfo):
    # clean pvinfo.config
    c = pvinfo['config']
    
    if len(c['raw_url']) == 1:
        c.pop('raw_url')
    to = [
        'rest', 
        'enable', 
        'disable', 
        'feature', 
        'comment', 
    ]
    for i in to:
        if len(c[i]) < 1:
            c.pop(i)
    # clean info
    i = pvinfo['info']
    if 'title_extra' in i:
        t = i['title_extra']
        if ('sub' in t) and (t['sub'] in ['', None]):
            t.pop('sub')
        if ('no' in t) and (t['no'] < 0):	# FIXME maybe BUG here
            t.pop('no')
        if ('short' in t) and (t['short'] in ['', None]):
            t.pop('short')
        if len(i['title_extra']) < 1:
            i.pop('title_extra')
    if ('vid_extra' in i) and (len(i['vid_extra']) < 1):
        i.pop('vid_extra')
    # clean pvinfo.video[].file[]
    for v in pvinfo['video']:
        for f in v['file']:
            if ('header' in f) and (len(f['header']) < 1):
                f.pop('header')
            if ('checksum' in f) and (len(f['checksum']) < 1):
                f.pop('checksum')
            if ('expire' in f) and (f['expire'] in ['', None]):
                f.pop('expire')
    # clean pvinfo._cache
    if ('_cache' in pvinfo) and (len(pvinfo['_cache']) < 1):
        pvinfo.pop('_cache')
    return pvinfo


def make_pvinfo_output(pvinfo):
    # TODO support fix_size
    
    pvinfo = json_clone(pvinfo)
    # add more data to pvinfo
    pvinfo['#'] = 'p_video/pvinfo struct'
    pvinfo['mark_uuid'] = PVINFO_MARK_UUID
    pvinfo['port_version'] = PVINFO_PORT_VERSION
    
    # make pvinfo.config
    pvinfo['config'] = _make_config()
    # add quality to pvinfo.video[]
    pvinfo = _add_quality(pvinfo, keep_raw_quality=var.feature['keep_raw_quality'])
    # make pvinfo.cache
    pvinfo['_cache'] = _make_cache()
    # add last_update
    pvinfo['last_update'] = gen_last_update()
    
    # check feature and clean data
    if var.feature['clean_output_pvinfo']:
        pvinfo = _clean_pvinfo(pvinfo)
    # TODO add empty values when not clean
    # check pretty print and restruct
    if var.feature['pretty_print']:
        pvinfo = pvinfo_pretty_print(pvinfo)
        # NOTE turn-off sort_key in final json-text print
        var.pretty_print_sort_key = False
    return pvinfo

# end _make_pvinfo_output.py


