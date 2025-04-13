def count_evens(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1

    return count        

def main():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        else:
            lst.append(int(user_input))
            count = count_evens(lst)

    print(f"You have entered {count} even numbers.")        
        
if __name__ == "__main__":
    main()       