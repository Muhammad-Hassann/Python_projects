MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        print('Removing', lst.pop())

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    
if __name__ == '__main__':
    main()