"""CP1404/CP5632 Practical - Car class example."""


class ProgrammingLanguage:  # Done.
    """Represent a ProgramingLanguage data in class."""

    def __init__(self, name='', typing='', reflection=False, year=0):
        """Initialise a ProgramingLanguage instance.


        name: str, represents ProgramingLanguage name.
        typing: str, represents ProgramingLanguage typing.
        reflection: bool, represents ProgramingLanguage reflection.
        year: int, represents ProgramingLanguage origin year.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Print this string format when called."""  # Done.
        # Done.
        return '{}, {}, Reflection={}, First appeared in {}'.format(self.name,
                                                                    self.typing,
                                                                    self.reflection,
                                                                    self.year)

    def is_dynamic(self):  # Done.
        """Add amount to the car's fuel."""
        if self.typing == 'Dynamic':
            return True
        else:
            return False
