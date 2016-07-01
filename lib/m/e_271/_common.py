# _common.py, p_video/lib/m/e_271/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 


def pure_url(raw):
    # FIXME maybe BUG here
    out = raw.split('#', 1)[0].split('?', 1)[0]
    return out


# end _common.py


