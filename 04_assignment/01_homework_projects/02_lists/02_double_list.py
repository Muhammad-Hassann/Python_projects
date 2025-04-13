def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(numbers)):
        index = numbers[i]
        numbers[i] = index * 2

    print(numbers)    
    
if __name__ == '__main__':
    main()