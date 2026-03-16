"""
Program Name: Die class
Name: Riddhi Agarwal
Starter code: none
Purpose: Creating a die class that creates a die with random number of sides, with the defualt being 6 sides.
Date: March 15, 2026
"""

import random

class Die:
    def __init__(self, sides: int = 6):
        "Initializes the dice with number of sides"
        self.sides: int = sides
    
    def roll_die(self):
        """Returns a random number between 1 and the number of sides the die has."""
        return random.randint(1, self.sides)
