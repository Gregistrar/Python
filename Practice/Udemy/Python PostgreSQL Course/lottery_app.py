"""
Lottery App
==================
The User picks 6 numbers
Lottery calculates 6 random numbers between 1 and 30
We match the user numbers to our lottery numbers
Calculate the winnings based on how many numbers matched
"""

import random


def menu():
    # Ask for player numbers, calculate winnings and print
    user_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched {}.\nYou won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))


def get_player_numbers():
    input_numbers = input("Enter your numbers, separated by commas (1-20): ")
    list_input = input_numbers.split(",")
    set_numbers = {int(number) for number in list_input}
    return set_numbers


def create_lottery_numbers():
    lottery_numbers = set()
    while len(lottery_numbers) < 6:
        lottery_numbers.add(random.randint(1, 20))
    return lottery_numbers


menu()

# print(get_player_numbers())
# print(create_lottery_numbers())



