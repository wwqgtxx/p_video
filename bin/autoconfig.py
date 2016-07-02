#!/usr/bin/env python3.5

AUTO_CONFIG = {
    '^http://[a-z]+\.iqiyi\.com/.+\.html' : [
        '-m', 'e_271', 
        '-e', 'm_pc_flash', 
    ], 
}

RE_SUPPORT_URL = [
    '^http://[a-z]+\.iqiyi\.com/.+\.html', 
]
SUPPORT_URL_BLACKLIST = [
    '\.iqiyi\.com/(lib/m|a_)', 
]