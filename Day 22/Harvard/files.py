#name = input("What's your name? ")

# method 1 - to work with files
"""
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""

# method 2 - using with function
"""
with open ("name.txt", "a") as file:
    file.write(f"{name}\n")
"""

# reading a file

with open ("name.txt", "r") as file:
    lines = file.readlines()