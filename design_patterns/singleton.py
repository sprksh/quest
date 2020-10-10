"""
Singletons are used loggers, 
initializing db connection, cache connetion etc at the start of the application 
and then importing it fo reuse is application of singleton pattern.

https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

Why use singleton: Mostly in multithreaded environment, you want some of the classes to 
be instantiated only once.
Python wouldn't need it much because we mostly do not use it that way.
In Python, when initiating an app, we create multiple processes as compared to let's say java,
where we create a threadpool, one out of which is assigned an incoming request.
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Bogger(metaclass=Singleton):
    def __init__(self, a):
        self.a = a

