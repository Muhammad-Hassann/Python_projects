my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range"

def modify_element(lst, index, val):
    if 0 <= index < len(lst):
        lst[index] = val
        return lst
    else:
        return "Index out of range"

def slicing(lst, start_index, end_index):
    if 0 <= start_index < len(lst) and 0 <= end_index <= len(lst):
        return lst[start_index:end_index]       
    else:
        return "Index out of range"

def main():
    while True:
        print("\nCurrent List:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            index = int(input("Enter the index to access: "))
            print("Element:", access_element(my_list, index))
        
        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = int(input("Enter the new value: "))
            result = modify_element(my_list, index, new_value)
            print("Updated List:", result)
        
        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slicing(my_list, start, end))
        
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
