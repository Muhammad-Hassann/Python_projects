def in_range(n, low, high):
    if n >= low and n <= high:
        return True

    return False    

def main():
    print(in_range(10, 5, 15))
    print(in_range(20, 5, 15))
    print(in_range(5, 5, 15))
    print(in_range(15, 5, 15))    

if __name__ == "__main__":
    main()    