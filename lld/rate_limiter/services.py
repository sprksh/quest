from rate_limiter import RateLimiterService, rate_limiter_decorator

rate_limiter = RateLimiterService()
print(rate_limiter.rate_limiter_buckets_dict)


class OrderService:
    service_name = "OrderService"

    def __init__(self):
        pass

    @rate_limiter_decorator(rate_limiter, service_name, "GET")
    def get(self):

        return

    @rate_limiter_decorator(rate_limiter, service_name, "POST")
    def post(self):

        return


class DeliveryService:
    service_name = "DeliveryService"

    def __init__(self):
        pass

    @rate_limiter_decorator(rate_limiter, service_name, "GET")
    def get(self):
        return

    @rate_limiter_decorator(rate_limiter, service_name, "POST")
    def post(self):
        return
