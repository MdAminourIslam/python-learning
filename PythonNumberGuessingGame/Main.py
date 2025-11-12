# Python Number Guessing Game
import random

lowest_num = 1
heighest_num = 100
answer = random.randint(lowest_num, heighest_num)

guesses = 0
is_running = True

print("----------Python Number Guessing Game---------")
print(f"Select a number between {lowest_num} and {heighest_num}")

while is_running:
    guess = input("Enter Your Guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > heighest_num:
            print("Your Guess is out of Range!!")
            print(f"Please Select a number between {lowest_num} and {heighest_num}")
        elif guess > answer:
            print("Too High! Try Again")
        elif guess < answer:
            print("Too Low! Try Again")
        else:
            print(f"CORRECT! The Answer was {answer}")
            print(f"Number of guesses {guesses}")
            is_running = False
    else:
        print("Invalid Gueess")
        print(f"Please Select a number between {lowest_num} and {heighest_num}")

