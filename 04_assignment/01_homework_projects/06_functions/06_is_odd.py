def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

def main():
    num = int(input("Enter a number: "))
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")        

if __name__ == "__main__":
    main()