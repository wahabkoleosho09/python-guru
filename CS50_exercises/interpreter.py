"""
a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a 
floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, 
with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, 
if y is /, then z will not be 0.
"""

Expressions = input("Expressions: ").strip()
a,operator,b = Expressions.split(" ")
a = int(a)
b = int(b)
if operator == "+":
    print(f"{(a + b):.1f}")
elif operator == "-":
    print(f"{(a - b):.1f}")
elif operator == "*":
    print(f"{(a * b):.1f}")
elif operator == "/":
    print(f"{(a / b):.1f}")
