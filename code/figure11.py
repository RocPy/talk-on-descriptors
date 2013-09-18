"""
Figure 11: Why dictionaries are needed
"""

from weakref import WeakKeyDictionary

class NonNegative(object):
    """A descriptor that forbids negative values"""
    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        # we get here when someone calls x.d, and d is a NonNegative instance
        # instance = x
        # owner = type(x)
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        # we get here when someone calls x.d = val, and d is a NonNegative instance
        # instance = x
        # value = val
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.data[instance] = value

class BrokenNonNegative(object):
    def __init__(self, default):
        self.value = default

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.value = value

class Foo(object):
    bar = BrokenNonNegative(5) 

# It seems to work!?
f = Foo()
try:
    f.bar = -1
except ValueError:
    print "Caught the invalid assignment"

# Uh, oh not in this case!
f = Foo()
g = Foo()

print "f.bar is %s\ng.bar is %s" % (f.bar, g.bar)
print "Setting f.bar to 10"
f.bar = 10
print "f.bar is %s\ng.bar is %s" % (f.bar, g.bar)  #ouch
