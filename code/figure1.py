"""
Figure 1: The type of manipulations that properties and descriptors modify
"""

f = Foo()

# Call custom methods when trying to access:
b = f.bar

# Call custom methods when trying to assign:
f.bar = c

# Call custom methods when trying to delete:
del f.bar
