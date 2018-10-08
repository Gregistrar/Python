import random

print("Welcome to Cows and Bulls! \nYou have to guess the number between 1,000 and 9,999.")

# number = random.randint(1000, 10000)
# guess = None
# count = 0

# This function compares the numbers to return cows or bulls from the user guess.
def compare_numbers(number, guess):
    cowbull = [0, 0]  # cows, then bulls
    for i in range(len(number)):
        if len(guess) < 4:
            print("Your guess must be 4 digits.")
            break
        elif number[i] == guess[i]:
            cowbull[0] += 1
        elif number[i] in guess:
            cowbull[1] += 1
    return cowbull


if __name__ == '__main__':
    playing = True
    number = str(random.randint(1000, 10000)) # generate a number between 1,000 and 9,999
    count_guesses = 0

    while playing:
        guess = input("What is your guess? ")
        if guess == "exit":
            break

        cowbullcount = compare_numbers(number, guess)
        count_guesses += 1

        if len(guess) < 4:
            print("Try again. \nType 'exit' to close the game.")
        elif cowbullcount[0] == 4:
            playing = False
            print("You win the game after %s guesses! The number was %s." % (str(count_guesses), str(number)))
            break
        else:
            print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
            print("Your guess isn't correct. Try again.")
