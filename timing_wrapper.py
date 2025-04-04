#/usr/bin/env python3
"""@timing decorator implementation

The decorator is used to time your functions with fancy log message
"""

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        time_start = time()
        result = f(*args, **kwargs)
        time_end = time()
        print('func:%r args:[%r %r] took: %2.4f sec' % \
          (f.__name__, args, kwargs, time_end - time_start))
        return result
    return wrap
