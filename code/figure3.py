"""
Figure 3: First attempt at catching edge conditions
"""
class Movie(object):
    def __init__(self, title, rating,
                 runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.gross = gross
        if budget < 0:
            raise ValueError("Negative value not \
                             allowed: %s" % budget)
        self.budget = budget

    def profit(self):
        return self.gross - self.budget

# m = Movie('Casablanca', 97, 102, 964000, 1300000)
