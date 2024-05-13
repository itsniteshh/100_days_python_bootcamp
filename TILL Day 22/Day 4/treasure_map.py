lin1 = ["x", "x", "x"]
lin2 = ["x", "x", "x"]
lin3 = ["x", "x", "x"]

map = [lin1, lin2, lin3]
print("Hiding your treasure! O marks the spot.")

position = input() #where do you want the treasure A, B, C Column
columns = position[0].lower()
rows = int(position[1])-1 # reducing the value by 1 to match list indexing

#converting alphabets into numbers for indexing using formulae
"""
  abc = ["a", "b", "c"]
  column = abs.index(columns)  
    
"""
#converting alphabets into numbers for indexing

if columns == "a":
    columns = 0
elif columns == "b":
    columns = 1  
elif columns == "c":
    columns = 2
    
map[rows][columns] = "O"

print(f"{lin1}\n{lin2}\n{lin3}")

