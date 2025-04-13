def add_numbers(numbers):
    sum_of_numbers = 0
    for i in range(len(numbers)):
        sum_of_numbers = numbers[i] + numbers[i]
    return sum_of_numbers

def main():
    numbers = [2, 9, 27, 3, 16, 22, 54]
    sum_of_numbers = add_numbers(numbers)

    print(sum_of_numbers)

if __name__ == '__main__':
    main()