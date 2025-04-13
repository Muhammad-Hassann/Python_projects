affirmation = "I am capable of doing anything I put my mind to."

def main():
    user_input = input(f"Please type the following affirmation: {affirmation}")
    while user_input != affirmation:
        print("That is not the affirmation. Please type the following affirmation: ")
        user_input = input()

    print("That's right! :)")
    
if __name__ == "__main__":
    main()    