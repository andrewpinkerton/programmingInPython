from random import randint


class Die:
    """Die class with a number of sides and a roll method."""

    def __init__(self, sides: int) -> None:
        """Create a new die with a number of sides."""

        self.sides = sides

    def roll(self) -> int:
        """Roll the die and return the result."""

        return randint(1, self.sides)
    
    def get_sides(self) -> int:
        """Return the number of sides of the die."""

        return self.sides
    
    def __str__(self) -> str:
        """Return string representation of the die."""

        return f"A {self.sides}-sided die."