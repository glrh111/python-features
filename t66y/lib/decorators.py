'''
define some decorators use in my own progs
'''
import time

def print_time(f):
    def wrapper(*args, **kwargs):
        print u'START AT: <%s>' % time.ctime()
        # rem return 
        return f(*args, **kwargs)
        print u'END   AT: <%s>' % time.ctime()
    return wrapper

