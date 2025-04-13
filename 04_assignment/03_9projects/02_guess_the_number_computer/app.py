import random


def guess(x):
    random_number = random.randint(1, x)
    user = 0
    while user != random_number:
        user = int(input(f"Guess the number between 1 to {x}: "))
        if user > random_number:
            print("Sorry, guess again. Too high!")
        elif user < random_number:
            print("Sorry, guess again. Too low!")

    print(f"Yay, congrats! You guessed the number {random_number} right!")
    
guess(50)