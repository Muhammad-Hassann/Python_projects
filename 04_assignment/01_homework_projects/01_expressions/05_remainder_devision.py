def main():
    dividend = int(input("Enter an integer to be divided: "))
    divisor = int(input("Enter an integer to divided by: "))
    result = dividend // divisor 
    remainder = dividend % divisor
    print(dividend, "divided by", divisor, "is", result, "with a remainder of", remainder)
if __name__ == '__main__':
    main()