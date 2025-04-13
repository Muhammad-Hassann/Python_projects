planets_gravity = {
    'mercury': 37.6,
    'venus': 88.9,
    'mars': 37.8,
    'jupiter': 236.0,
    'saturn': 108.1,
    'uranus': 81.5,
    'neptune': 114.0
}

def main():
    weight = float(input('Enter a weight on earth: '))
    planet = input('Enter a planet: ').lower()
    gravity = planets_gravity.get(planet)
    if gravity:
        weight_on_planet = weight * gravity / 100
        print(f'The equivalent weight on {planet} is {weight_on_planet}')
    else:
        print('Invalid planet name')

if __name__ == '__main__':
    main()        