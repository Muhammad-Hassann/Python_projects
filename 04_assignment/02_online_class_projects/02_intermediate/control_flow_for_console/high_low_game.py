import random

def main():

    NUM_ROUNDS = 1
    SCORE = 0

    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    while NUM_ROUNDS != 6:

        USER_NUMBER = random.randint(1, 100)
        COMPUTER_NUMBER = random.randint(1, 100)

        print(f"Round {NUM_ROUNDS}")
        print(f"Your number is {USER_NUMBER}")

        high_low = input("Do you think your number is higher or lower than the computer's?: ")
        
        if high_low == "higher" and USER_NUMBER > COMPUTER_NUMBER:
            print(f"You were right!\n The computer's number was {COMPUTER_NUMBER}")
            SCORE += 1
        elif high_low == "lower" and USER_NUMBER < COMPUTER_NUMBER:
            print(f"You were right!\n The computer's number was {COMPUTER_NUMBER}")
            SCORE += 1
            
        elif high_low != "higher" and high_low != "lower":
            print("Please enter either higher or lower:")
            continue    
        else:
            print(f"Aww that's incorrect!\n The computer's number was {COMPUTER_NUMBER}")

        print("Your score is now", SCORE)
        NUM_ROUNDS += 1

    print("Your final score is", SCORE)

    if SCORE == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif SCORE > NUM_ROUNDS // 2:``
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")    
    

if __name__ == "__main__":
    main()