#program to decide bill payer
names_input = input("Enter frnds name followed by comma\n")

#splitting names from input to a list
names = names_input.split(", ")

import random

select = random.randint(0, len(names)-1)

payer = names[select]

print(f"Today's bill will be sponsored by {payer}")