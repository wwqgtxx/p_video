# _log.py, p_video/lib/util/
# LICENSE GNU GPLv3+: Copyright (C) 2016  sceext <sceext@foxmail.com> 

import sys


def get_caller_info(depth=2):
    f = sys._getframe(depth)
    out = {
        'module' : f.f_globals['__name__'], 
        'function' : f.f_code.co_name, 
    }
    return out


class Log(object):
    
    def __init__(self):
        self.out = sys.stderr.buffer
        self.flush = True
        self.use_blob = True	# write utf-8 blob, not print text
        
        self.log_module = False
        self.log_function = False
        self.log_debug = True
        
        self.quiet_mode = False	# NOT log WARNING, INFO, OK, only print ERROR
        
        self.log_prefix = 'pv::'
    
    # low-level print function
    def _lp(self, text):
        if self.use_blob:
            text = text.encode('utf-8')
        self.out.write(text)
        if self.flush:
            self.out.flush()
    # prefix-print function
    def _pp(self, text, prefix='', end='\n', depth=0):
        base_depth = 3	# NOTE base_depth should be 3
        caller_info = get_caller_info(depth = depth + base_depth)
        
        module = ''
        function = ''
        if self.log_module:
            module = caller_info['module']
            if self.log_function:
                function = '#' + caller_info['function']
        to = self.log_prefix + module + function
        to += prefix + text + end
        
        self._lp(to)
    # exports function
    
    # print raw text (without prefix)
    def p(self, text, *k, **kk):
        self._pp(text, prefix=':', *k, **kk)
    
    # ERROR, NOTE `error` will always be print
    def e(self, text, *k, **kk):
        self._pp(text, prefix='  !!! ERROR: ', *k, **kk)
    
    # WARNING, check `quiet` mode
    def w(self, text, *k, **kk):
        if not self.quiet_mode:
            self._pp(text, prefix='  ! WARNING: ', *k, **kk)
    # OK, check `quiet` mode
    def o(self, text, *k, **kk):
        if not self.quiet_mode:
            self._pp(text, prefix='  [ OK ] ', *k, **kk)
    # INFO, check `quiet` mode
    def i(self, text, *k, **kk):
        if not self.quiet_mode:
            self._pp(text, prefix='  (i) ', *k, **kk)
    # DEBUG, check log_debug
    def d(self, text, *k, **kk):
        if self.log_debug:
            self._pp(text, prefix='  (debug) ', *k, **kk)
    # end Log class

# exports: global default log object
log = Log()

# end _log.py


