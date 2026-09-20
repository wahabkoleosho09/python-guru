# E = mc^2

c = 300000000  # speed of light in m/s

def energy(mass):
    return mass * c ** 2

def main():
    m = int(input("Enter mass in kilograms: "))
    e = energy(m)
    print(e)

main()
