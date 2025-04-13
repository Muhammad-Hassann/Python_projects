def main():
    mass = float(input("Enter mass in Kg: "))
    speed = 299792458
    energy = mass * speed ** 2

    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(speed) + " m/s")

    print("The energy in Joules is:", energy)

if __name__ == '__main__':
    main()