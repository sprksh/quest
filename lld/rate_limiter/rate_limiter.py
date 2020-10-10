from .infrastructure import Limit
from collections import deque
from datetime import datetime, timedelta
import json


class RateLimiterFactory:

    @staticmethod
    def create_rate_limiter_buckets(rate_limits):
        rate_limiter_buckets = {}
        for entry in rate_limits["serviceLimits"]:
            service_name = entry["service"]
            global_limit = entry["globalLimits"]
            # api_limits = entry.get("apiLimits")
            rate_limiter_buckets.setdefault(service_name, {})["global"] = RateLimiterFactory._create_limiters(
                global_limit)
            # rate_limiter_buckets.setdefault(service_name, {})["api"] = RateLimiterService._create_limiters(api_limits)
        return rate_limiter_buckets

    @staticmethod
    def _create_limiters(limit):
        method_bucket_dict = {}
        for method, data in limit.items():
            method_bucket_dict[method] = RateLimiter(data["granularity"], data["limit"])
        return method_bucket_dict




class RateLimiter:
    def __init__(self, granularity, request_limit):
        self.bucket = deque()
        self.granularity = self.set_granularity(granularity)
        self.request_limit = request_limit

    @staticmethod
    def set_granularity(granularity):
        if granularity == "minute":
            return 60
        if granularity == "second":
            return 1
        if granularity == "hour":
            return 60*60

    def rate_limit(self):
        """
        returns False if rate limit exceeded, otherwise adds to the bucket
        :return:
        """
        # import ipdb; ipdb.set_trace()
        current_time = datetime.now()
        if self.check_if_limit_exceeded(current_time):
            return False

        return True

    def add_time(self):
        current_time = datetime.now()
        self.bucket.append(current_time)
        return

    def check_if_limit_exceeded(self, current_time):
        while self.bucket and self.bucket[0] <= current_time - timedelta(seconds=self.granularity):
            self.bucket.popleft()
        if len(self.bucket) >= self.request_limit:
            return True
        return False


# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]

class RateLimiterService:
    """
    1. it will create the entire nested dict of limiters on initiation
        {
          "service_name": {
            "global": {
              "get": RateLimiter,
              "post": RateLimiter
            },
            "api": {
              "get": RateLimiter,
              "post": RateLimiter
            },
          }
        }


    2. single function which takes service, method and calls respective
    """
    def __init__(self):
        self.rate_limits = json.loads(Limit.limit_json)
        self.rate_limiter_buckets_dict = RateLimiterFactory.create_rate_limiter_buckets(self.rate_limits)

    def get_rate_limiters_for_api(self, service, method):
        global_data = self.rate_limiter_buckets_dict[service].get("global")
        api_data = self.rate_limiter_buckets_dict[service].get("api")

        global_limiter = global_data[method]
        api_limiter = api_data[method] if api_data else None
        return global_limiter, api_limiter

    def check_rate_limit_by_hierarchy(self, service, method):
        global_limiter, api_limiter = self.get_rate_limiters_for_api(service, method)

        if not global_limiter.rate_limit():
            return False
        if api_limiter and not api_limiter.rate_limit():
            return False
        global_limiter.add_time()
        if api_limiter:
            api_limiter.add_time()
        return True

    def rate_limit(self, service, method):
        return self.check_rate_limit_by_hierarchy(service, method)


def rate_limiter_decorator(rate_limiter, service, method):
    def decorator(f):
        print(f)
        def _wrapper(*args, **kwargs):
            if not rate_limiter.rate_limit(service, method):
                print("Limit exceeded")
                raise Exception("Limit Exceeded")
            else:
                print("Limit not exceeded")
            return f(*args, **kwargs)
        return _wrapper

    return decorator
