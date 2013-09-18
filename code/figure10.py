"""
Figure 10: How not to do descriptors!
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

class Broken(object):
    y = NonNegative(5)
    def __init__(self):
        self.x = NonNegative(0)  # NOT a good descriptor

# Accessing the class-level descriptor y automatically calls __get__.
# However, accessing the instance-level descriptor x returns the descriptor itself
b = Broken()
print "X is %s, Y is %s" % (b.x, b.y)
