"""Store guitar data."""


class Guitar:
    # Done.
    def __init__(self, name='', year=0, cost=0):
        """initialise Guitar class.

        name: str, represents the name of Guitar.
        year: int, represents the year of Guitar.
        cost: float, represents the cost of Guitar.
        """

        self.name = name
        self.year = year
        self.cost = cost

    # Done.
    def __str__(self):
        """Print this string format when called."""
        return '{} ({}) : ${}'.format(self.name, self.year, self.cost)

    # Done.
    def get_age(self):
        """Return age of guitar."""
        age = 2021 - self.year
        return age

    # Done.
    def is_vintage(self):
        """Return True if vintage, else False."""
        age = 2021 - self.year
        if age >= 50:
            return True
        else:
            return False
