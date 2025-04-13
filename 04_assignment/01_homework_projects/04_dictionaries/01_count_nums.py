def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict

def print_nums(num_dict):
    for num, count in num_dict.items():
        print(f"{num} appears {count} time(s)")            

def main():
    num_lst = []
    while True:
        num = input("Enter a number (or press Enter to finish): ")
        if num == "":
            break
        num_lst.append(int(num))
    num_dict = count_nums(num_lst)
    print_nums(num_dict)
    print(num_dict)
    print(num_lst)
    
    
if __name__ == '__main__':
    main()