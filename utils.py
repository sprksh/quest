import functools
import time
import math


def timer():
    """
    Decorator to log timings
    """

    def decorator(func):
        @functools.wraps(func)
        def _timer(*args, **kwargs):
            ret = None
            st = time.time()
            start_time = math.ceil(st * (10 ** 5)) / (10 ** 2)
            ret = func(*args, **kwargs)
            et = time.time()
            response_time = math.ceil((et - st) * (10 ** 5)) / (10 ** 2)
            print("--func %s time to execute: %s" % (func, response_time))
            return ret

        return _timer

    return decorator


