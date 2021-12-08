#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Dec. 7, 2021
# This program determines if a user has
# guessed the magic number.

import constants


def main():
    # this function checks if the user has
    # entered the correct number

    # input
    user_number = int(input("Enter an integer number between 0 and 9: "))
    print("")

    # process & output
    if user_number == constants.MAGIC_NUMBER:
        print("You are correct, congratulations!")
    else:
        print("You are wrong!")


if __name__ == "__main__":
    main()
