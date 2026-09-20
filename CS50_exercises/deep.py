"""
a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
Otherwise output No
"""

user = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
if user == "forty-two" or user == "forty two" or user == "42":
    print("Yes")
else:
    print("No")
