# var.py, p_video/lib/

from .conf import get_feature_init


class Var(object):
    '''
    p_video global data
    
    NOTE data from command line arguments or stdin will be directly here
    '''
    def __init__(self):
        # init feature value (default)
        self.feature = get_feature_init()
        
        # command line data
        self.debug = False	# --debug, global debug (low-level) flag
        self.comment = None	# --comment TEXT
        
        self.module = None	# -m, --module MODULE
        self.entry = None	# -e, --entry ENTRY
        
        self.rest = []	# --, rest command line arguments
        
        # raw stdin data
        self.raw_stdin = None
        
        self.cache = {}		# global module/entry cache
        self.m = None		# module object (single module in p_video)
        self.mvar = None	# module var object
        
        # TODO
    # end Var class

var = Var()	# exports
# end var.py


