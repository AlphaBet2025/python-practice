"""
PROJECT 4 (simplified): PASSWORD GENERATOR
============================================
Teaches: the `string` module, and building a string one random
character at a time using a loop.
"""

import random
import string

# These are just pre-made strings Python gives you for free:
letters = string.ascii_letters   # "abcdefg...XYZ"
digits = string.digits           # "0123456789"
symbols = "!@#$%^&*"             # a few symbols, kept short on purpose

# Combine them into one big pool of possible characters
all_characters = letters + digits + symbols


def generate_password(length):
    password = ""  # start with an empty string
    for i in range(length):
        # pick ONE random character from the pool and add it on
        random_char = random.choice(all_characters)
        password = password + random_char
    return password


def main():
    print("=== Password Generator ===")
    length = int(input("How long should the password be? "))
    password = generate_password(length)
    print("Your password:", password)


if __name__ == "__main__":
    main()
