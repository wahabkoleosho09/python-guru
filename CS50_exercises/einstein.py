"""
a program in Python that prompts the user for mass as an integer (in kilograms) and 
then outputs the equivalent number of Joules as an integer. 
Assume that the user will input an integer.
"""

# E = mc^2

c = 300000000  # speed of light in m/s

def energy(mass):
    return mass * c ** 2

def main():
    m = int(input("Enter mass in kilograms: "))
    e = energy(m)
    print(e)

main()
