"""
Adds behaviour to an object at runtime.

Wrapping object with a decorator

Different from python decorator: Decorator adds behaviour at definition time while decorator pattern
adds behaviour at runtime.

"""

class foo(object):
    def f1(self):
        print("original f1")
    
    def f2(self):
        print("original f2")

class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def __getattr__(self, name):
        return getattr(self._decoratee, name)
    
    def f1(self):
        print("decorated f1")
        self._decoratee.f1()
    
u = foo()
v = foo_decorator(u)
v.f1()
v.f2()
