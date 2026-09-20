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
