import random

from art import logo
EASY_TURNS = 10
HARD_TURNS = 5


def guess(user_guess, system_number):
    if user_guess > system_number:
        print("Too High!!")
    elif user_guess < system_number:
        print("Too Low!!")
    else:
        print(f"You Got it the number was {user_guess}")
        return 0


def set_difficulty():
    difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ")
    global max_attempts
    if difficulty.lower() == 'easy':
        return EASY_TURNS
    else:
        return HARD_TURNS


print(logo)
print("Welcome to the number guessing Game!!")
print("I'm thinking of a number between 1 and 100.")
max_attempts = set_difficulty()
system_number = random.randint(1, 100)

while max_attempts > 0:
    print(f"you have {max_attempts} remaining to guess the number")
    user_guess = int(input("Make a guess: "))
    output = guess(user_guess,system_number)
    if output == 0:
        break
    max_attempts -= 1

