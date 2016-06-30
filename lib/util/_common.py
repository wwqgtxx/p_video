# _common.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

import json
import hashlib


def hash_md5(raw):
    
    # TODO
    pass


def json_clone(raw):
    return json.loads(json.dumps(raw))

def json_cmp(a, b):
    def print_one(raw):
        return json.dumps(raw, sort_keys=True, ensure_ascii=False)
    return (print_one(a) == print_one(b))

def json_print(raw, sort_key=True, fix_unicode=False):
    return json.dumps(raw, indent=4, sort_keys=sort_key, ensure_ascii=fix_unicode)


# end _common.py


