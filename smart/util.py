# -*- coding: utf-8 -*-
import functools
import time
import sys

def cost_time(arg):
    """Decorator for calculating how much time spended, while calling a function.
    Usage:
      >>> @cost_time
      ... def hello(text):
      ...     time.sleep(1)
      ...     print "hello {}".format(text)
      >>> hello("world")
      hello world
      Function: hello, Cost time: 1.00s

      # Redirect output tip to handler, 
      # default is stand output(sys.stdout).
      >>> from StringIO import StringIO
      >>> f = StringIO() 
      >>> @cost_time(f)
      ... def hello(text):
      ...     time.sleep(1)
      ...     print "hello {}".format(text)
      >>> hello("world")
      hello world

      >>> print f.getvalue().strip()
      Function: hello, Cost time: 1.00s

    """
    def decorator(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            start = time.time()
            output = func(*args, **kwargs)
            end = time.time()
            tip = "Function: {}, Cost time: {:.2f}s".format(func.__name__, end - start) 
            print >> handler, tip 
            return output
        return wrap

    if callable(arg):
        handler = sys.stdout
        return decorator(arg)
    else:
        handler = arg
        if hasattr(handler, "write"):
            return decorator
        else:
            raise ValueError("'{}' object has no method 'write'.".format(type(handler).__name__))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

