def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total_cost = 0

    for fruit, price in fruits.items():
        fruit_count = int(input(f"How many ({fruit}) do you want? ")) 
        total_cost += (price * fruit_count)

    print("Your total is", "$",total_cost)    

if __name__ == '__main__':
    main()        