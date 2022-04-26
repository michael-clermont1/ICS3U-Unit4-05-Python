#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is calculates the sum of positive numbers


def main():
    # this function calculates the sum of positive numbers
    counter = 0
    sum_of_numbers = 0
    # input
    number_as_string = input("How many numbers are you going to add: ")
    # process & output
    print("")
    try:
        number_as_int = int(number_as_string)
        for counter in range(number_as_int):
            num = int(input("Enter a number to add: "))
            counter = counter + 1
            if num > 0:
                sum_of_numbers = sum_of_numbers + num
                continue
            else:
                continue
        print("\nThe sum is {0}".format(sum_of_numbers))
    except Exception:
        print("That is not a integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
