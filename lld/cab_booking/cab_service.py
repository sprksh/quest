class User:
    def __init__(self, name):
        self.name = name
        self.average_rating = 0
        self.total_trips = 0
        self.total_ratings = 0
        self.ratings = []
        self.one_rating_users = set()

    def rate(self, rating, from_user):
        if rating == 1:
            self.one_rating_users.add(from_user)
        self.ratings.append(rating)
        self.total_ratings += 1
        self.average_rating = (self.average_rating * (self.total_ratings-1) + rating)/self.total_ratings

class CabDriver(User):
    def __init__(self):
        self.status = None
        self.current_location = None
    

class Customer(User):
    def __init__(self):
        pass

    

class Trip:
    def __init__(self, customer, driver):
        self.customer = customer
        self.driver = driver
        self.driver_rating = None
        self.customer_rating = None
        self.source = None
        self.destination = None

    def rate_user(self, to_user, from_user, rating):
        if to_user == self.driver and from_user == self.customer:
            self.driver.rate(rating)
        
        if to_user == self.customer and from_user == self.driver:
            self.customer.rate(rating)

    def start_trip(self):
        pass
    
    def end_trip(self):
        pass


class CabService:
    def __init__(self, customer):
        self.customer = customer
    
    def request_cab(self):
        pass

    def match_cab(self):
        pass

    def start_ride(self):
        pass
    
    def end_ride(self):
        pass
    

