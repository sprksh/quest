from services import OrderService, DeliveryService
import time


class TestRateLimiter:
    def __init__(self):
        self.order_service = OrderService()
        self.delivery_service = DeliveryService()

    def test_rate_limits_on_order_get(self):
        order_service = OrderService()
        for i in range(11):
            # if i == 10:
            #     time.sleep(1)
            order_service.get()

    def test_rate_limits_on_order_post(self):
        pass

    def test_rate_limits_on_delivery_get(self):
        pass

    def test_rate_limits_on_delivery_post(self):
        pass


# if __name__ == "__main__":
test_limits = TestRateLimiter()
test_limits.test_rate_limits_on_order_get()
