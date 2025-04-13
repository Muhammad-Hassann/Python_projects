import random
def main():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print("Rolling the dice...")
    print("Die 1:", die1)
    print("Die 2:", die2)
    print("Total value:", total)
if __name__ == '__main__':
    main()