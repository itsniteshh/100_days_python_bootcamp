
filename = "name.txt"
name = input("What's your name: ")

with open(filename, "w") as files:
    files.write(name)

print(name)

