# _select_hd_i.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

from ..var import var


def count_video(pvinfo):
    for v in pvinfo['video']:
        count_size_byte = True
        count_time_s = True
        # check to skip video
        if ('size_byte' in v) and (v['size_byte'] > 0):
            count_size_byte = False
        if ('time_s' in v) and (v['time_s'] > 0):
            count_time_s = False
        count_one_video(v, count_size_byte=count_size_byte, count_time_s=count_time_s)
    return pvinfo

def count_one_video(v, count_size_byte=True, count_time_s=True):
    size_byte = 0
    time_s = 0
    for f in v['file']:
        if (size_byte >= 0) and (f['size_byte'] > 0):
            size_byte += f['size_byte']
        else:
            size_byte = -1
        if (time_s >= 0) or (f['time_s'] > 0):
            time_s += f['time_s']
        else:
            time_s = -1
    # save result
    if (not 'size_byte' in v) or count_size_byte:
        v['size_byte'] = size_byte
    if (not 'time_s' in v) or count_time_s:
        v['time_s'] = time_s
    # set `count`
    if (not 'count' in v) or (v['count'] <= 0):
        v['count'] = len(v['file'])
    # done, return None


def select_hd_i(pvinfo):
    # get hd, i limit from var.feature
    hd = var.feature['hd']
    i = var.feature['i']
    
    for v in pvinfo['video']:
        # select hd
        if (hd[0] != None) and (v['hd'] < hd[0]):	# hd_min
            v['file'] = []
        if (hd[1] != None) and (v['hd'] > hd[1]):	# hd_max
            v['file'] = []
        # select i
        for j in range(len(v['file'])):
            ignore_i = False
            if (i[0] != None) and (j < i[0]):	# i_min
                ignore_i = True
            if (i[1] != None) and (j > i[1]):	# i_max
                ignore_i = True
            if ignore_i:
                v['file'][j]['url'] = ''
    return pvinfo

# end _select_hd_i.py


