MY_LIST = []

def main():
    value = input("Enter a value: ")
    while value != "":
        MY_LIST.append(value)
        value = input("Enter a value: ")

    print("Here's the list:", MY_LIST)

if __name__ == '__main__':
    main()