# love calc program

print("The Love Calculator will calculate your  score... please provide us with some details first")

name1 = input("Enter your name\n").lower()
name2 = input("Enter their name\n").lower()

# counting occurance and summing them
T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")
E = name1.count("e") + name2.count("e")

L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")
E = name1.count("e") + name2.count("e")

#storing occurance in variables
first_score = T + R + U + E
second_score = L + O + V + E

#converting data to str to concat and then summing them
final_score = int(str(first_score) + str(second_score))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos")
elif final_score > 40 and final_score < 50:
    print(f"Your score is {final_score}, you both go alright together")
else:
    print(f"Your score is {final_score}")

# NOTE - we cn combine names together to avoid double counting 