user = input("Greetings: ").strip().lower()

if user.startswith("hello") or "hello" in user:
    print("$0")
elif user.startswith("h"):
    print("$20")
else:
    print("$100")
