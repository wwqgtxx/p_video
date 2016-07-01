# help.py, p_video/lib/cli/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

def get_help():
    # TODO support `--help XXX` help items
    out = '''\
Usage: pv [OPTION]... URL  [-- ...]
       pv [--help|--version|--license]
p_video: parse to get video info from some web sites. 

  -m, --module MODULE  set module (name) to use
  -e, --entry ENTRY    set entry (name) to use
  
  -E, --enable FEATURE-A[,B]...   enable features (set to `true`)
  -D, --disable FEATURE-A[,B]...  disable features (set to `false`)
  
  -s, --set FEATURE-X=VALUE  set value (can use json str) of a feature
  
  -j, --set-json         input json info from stdin
  -#, --comment COMMENT  set comment text
      --                 pass all REST arguments to module

      --debug    enable low-level debug
      --help     display this help and exit
      --version  output version information and exit
      --license  show license information and exit

More information online: <https://github.com/sceext2/p_video> \
'''
    return out


# end help.py


