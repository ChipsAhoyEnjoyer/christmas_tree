from math import ceil
import os
import random

# TODO: Create tests
GREETINGS = [
    "Ho ho ho",
    "Generating holiday spirit",
    "Merry Chrysler",
]


def main() -> int:
    while True:
        response = input("Enter a size for your tree:\n")
        try:
            tree = int(response)
        except ValueError:
            print("Please enter a valid number...")
        else:
            if tree < 1:
                print("Trees can't be that short!")
            else:
                break

    os.system('cls' if os.name == 'nt' else 'clear')
    print(random.choice(GREETINGS) + "...\n\n")

    for leaf in range(1, tree+1):
        stars = "*" * (leaf * 2 - 1)
        spaces = " " * (tree - leaf)
        print(spaces + stars)

    trunk_size = tree//3 * 2 - 1
    trunk_space = " " * (tree - ceil(trunk_size/2))
    trunk = "*" * trunk_size
    for _ in range(tree//3):
        print(trunk_space + trunk)

    while True:
        try_again = input("\n\nType 'Rudolph' to try again, type 'Grinch' to exit the program:\n")
        if try_again.lower() == "rudolph":
            return 1
        elif try_again.lower() == "grinch":
            print("Have a merry christmas and a happy new year!")
            return 0
        else:
            print("Try again")


if __name__ == "__main__":
    loop = main()
    while loop == 1:
        loop = main()
