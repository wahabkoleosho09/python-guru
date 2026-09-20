"""
 A program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. 
 If the greeting starts with an “h” (but not “hello”), output $20. 
 Otherwise, output $100
"""
user = input("Greetings: ").strip().lower()

if user.startswith("hello") or "hello" in user:
    print("$0")
elif user.startswith("h"):
    print("$20")
else:
    print("$100")
