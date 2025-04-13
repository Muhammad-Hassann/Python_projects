stock = {
    "apple": 10,
    "banana": 5,
    "orange": 7,
    "pear": 3,
    "grape": 7,
}

def num_in_stock(fruit):
   
    if fruit in stock:
        print("This fruit is in stock. Here is how many")
        print(stock[fruit])
    else:
        print("This fruit is not in stock")

def main():
    while True:
        fruit = input("What fruit do you want to check? ")
        num_in_stock(fruit)
        if fruit == "":
            break

if __name__ == "__main__":
    main()