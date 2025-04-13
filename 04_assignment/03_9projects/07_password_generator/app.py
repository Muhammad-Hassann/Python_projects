import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
special_characters = string.punctuation
numbers = string.digits

number_of_passwords = int(input("Enter the number of passwords to generate: "))
length = int(input("Enter the length of the password: "))

print("\nHere are your passwords: ")

for pwd in range(number_of_passwords):
    password = ""
    for c in range(length):
        password += random.choice(uppercase_letters + lowercase_letters + special_characters + numbers)
    print(password)

