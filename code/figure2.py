"""
Figure 2: A simple movie class
"""

class Movie(object):
    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    def profit(self):
        return self.gross - self.budget
