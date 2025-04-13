def create_phonebook():
    phonebook = {}

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        number = input("Enter phone number: ")
        phonebook[name] = number

    return phonebook

def lookup_phonebook(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print(f"{name} not found in phonebook")

def print_phonebook(phonebook):
    for name, number in phonebook.items():
        print(f"{name}: {number}")

def main():
    phonebook = create_phonebook()
    lookup_phonebook(phonebook)
    print_phonebook(phonebook)

if __name__ == "__main__":
    main()    