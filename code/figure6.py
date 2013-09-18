"""
Figure 6: Property tedium. There is a lot of duplicated logic. While properties
          make the outsides of classes look nice, they don't make the insides
          of classes look nice.
"""

class Movie(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self._rating = None
        self._runtime = None
        self._budget = None
        self._gross = None

        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.gross = gross
        self.budget = budget

    #nice
    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._budget = value

    # No problem.
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._rating = value

    # Seriously?
    @property
    def runtime(self):
        return self._runtime

    @runtime.setter
    def runtime(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._runtime = value        

    # Please stop!
    @property
    def gross(self):
        return self._gross

    @gross.setter
    def gross(self, value):
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._gross = value        

    def profit(self):
        return self.gross - self.budget
