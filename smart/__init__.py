# -*- coding: utf-8 -*-

"""
Python Util library
~~~~~~~~~~~~~~~~~~~~~
"""

__title__ = 'Python Util Library'
__version__ = '0.0.1'
__author__ = 'jchluo'


#import api
from smart.util import cost_time

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
