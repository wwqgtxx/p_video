# _common.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

import json
import hashlib


def hash_md5(raw):
    return hashlib.md5(bytes(raw, 'utf-8')).hexdigest()


def json_clone(raw):
    return json.loads(json.dumps(raw))

def json_cmp(a, b):
    def print_one(raw):
        return json.dumps(raw, sort_keys=True, ensure_ascii=False)
    return (print_one(a) == print_one(b))

def json_print(raw, sort_key=True, fix_unicode=False):
    return json.dumps(raw, indent=4, sort_keys=sort_key, ensure_ascii=fix_unicode)


def merge_dict_obj(a, b):	# merge b in a
    if not isinstance(a, dict):
        return b
    out = a	# a must be a {} (dict)
    for key in b:
        if (key in a) and isinstance(a[key], dict):
            out[key] = merge_dict_obj(a[key], b[key])	# NOTE merge sub
        else:
            out[key] = b[key]
    return out


# end _common.py


