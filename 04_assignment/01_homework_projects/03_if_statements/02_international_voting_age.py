def main():
    age = int(input("How old are you?: "))
    if age < 0:
        print("Enter a valid age.")
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
    elif age >= 25:
        print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
    elif age >= 48:
        print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
        
if __name__ == '__main__':
    main()