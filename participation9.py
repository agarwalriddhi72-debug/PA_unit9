"""
Program Name: Dice Rolling program
Name: Riddhi Agarwal
Starter code: none
Purpose: uses the die class to roll dice with different number of sides.
Date: March 15, 2026
"""

from die import Die

def main():
    six_side_die: Die = Die()
    ten_side_die: Die = Die(10)
    twenty_side_die: Die = Die(20)

    print("Rolling a 6 sided die: ")
    for i in range(10):
        print(six_side_die.roll_die())

    print("\nRolling a 10 sided die: ")
    for i in range(10):
        print(ten_side_die.roll_die())
        
    print("\nRolling a 20 sided die: ")
    for i in range(10):
        print(twenty_side_die.roll_die())
    
if __name__ == "__main__":
    main()