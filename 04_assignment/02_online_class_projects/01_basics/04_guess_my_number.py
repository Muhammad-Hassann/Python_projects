import random

RANDOM_NUMBER = random.randint(1, 100)

def main():
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == RANDOM_NUMBER:
            print("You guessed it!")
            break
        elif guess < RANDOM_NUMBER:
            print("You guess it too low")
        else:
            print("You guess it too high")
if __name__ == '__main__':
    main()