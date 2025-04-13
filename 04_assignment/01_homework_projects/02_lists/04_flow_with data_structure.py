def add_three_copies(a_list, an_element):
    for i in range(3):
        a_list.append(an_element)

def main():
    message = input("Enter a message: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after", my_list)
    
if __name__ == '__main__':
    main()