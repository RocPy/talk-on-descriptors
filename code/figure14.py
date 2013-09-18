"""
Figure 14: Fragility of labeling descriptors
"""
class Descriptor(object):

    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        print '__get__', instance, owner
        return instance.__dict__.get(self.label)

    def __set__(self, instance, value):
        print '__set__'
            instance.__dict__[self.label] = value

class Foo(object):
    x = Descriptor('y')

f = Foo()
f.x = 5
print f.x
    
f.y = 4    #oh no!
print f.x
