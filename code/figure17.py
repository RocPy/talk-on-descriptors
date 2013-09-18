"""
Figure 16: A (read-only) descriptor decorator!
"""

class Property(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, type):
        if obj is None:
            return self
        return self.fget(obj)

class MyClass(object):
    @Property
    def foo(self):
        return "Foo!"
