# var.py, p_video/lib/

from .conf import get_feature_init


class GVar(object):
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
        self.raw_url = []	# raw input URLs
        
        self.cli_config = {}	# command line config object to output
            # used with --set-json (stdin input json)
        
        # raw stdin data
        self.raw_stdin = None
        self.raw_json = None	# json data input from stdin
        
        self.cache = {}		# global module/entry cache
        self.m = None		# module object (single module in p_video)
        self.mvar = None	# module var object
        
        # output (print stdout) result flag
        self.pretty_print_sort_key = True	# json.dumps(sort_keys=), should set to false after pretty_print restruct (OrderedDict)
    # end GVar class

var = GVar()	# exports
# end var.py


