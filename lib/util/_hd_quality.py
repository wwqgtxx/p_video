# _hd_quality.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 
'''
TODO

'''

import math


HD_TO_QUALITY = {
    9999 : '[溢出] 清晰度太高[坏笑]', 
    
    22 : '16K', 
    11 : '8K', 
    
    8 : '高码4K', 
    7 : '4K', 
    
    5 : '高码1080p', 
    4 : '1080p', 
    
    2 : '720p', 
    
    0 : '普清', 
    -1 : '低清', 
    
    -3 : '渣清', 
    -4 : '超渣', 
    -5 : '极其渣', 
    -6 : '无语渣', 
    -7 : '渣的无法形容', 
    
    -9 : '[溢出] 清晰度太低[汗]', 
}


def get_quality(hd):
    hd = float(hd)
    quality = HD_TO_QUALITY.get(math.floor(hd), None)
    if quality != None:
        return quality
    # check hd overflow
    min_hd, max_hd = min(HD_TO_QUALITY.keys()), max(HD_TO_QUALITY.keys())
    if hd <= min_hd:
        return HD_TO_QUALITY[min_hd]
    if hd >= max_hd:
        return HD_TO_QUALITY[max_hd]
    # get a closest
    c_hd = min_hd
    for i in HD_TO_QUALITY:
        if (i < hd) and (i > c_hd):
            c_hd = i
    return HD_TO_QUALITY[c_hd]

# end _hd_quality.py


