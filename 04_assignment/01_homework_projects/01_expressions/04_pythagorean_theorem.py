import math

def main():
    ab = float(input("Enter the lenght of AB: "))
    ac = float(input("Enter the lenght of AC: "))

    bc = math.sqrt(ab**2 + ac**2)
    print("The lenght of BC is:", bc)

if __name__ == '__main__':
    main()