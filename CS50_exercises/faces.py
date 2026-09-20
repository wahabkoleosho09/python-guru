def convert():
    greetings = input(": ")
    if ":)" in greetings:
        greetings = greetings.replace(":)", "🙂")
    if ":(" in greetings:
        greetings = greetings.replace(":(", "🙁")
    return greetings

def main():
    print(convert())

if __name__ == "__main__":
    main()
