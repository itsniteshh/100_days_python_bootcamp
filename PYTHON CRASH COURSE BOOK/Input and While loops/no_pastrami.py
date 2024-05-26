sandwich_orders = ["pastrami", "chicken crispy", "mushroom fry", "pastrami", "mix veggie", "pastrami"]
finished_sandwiches = []


print("Deli has run out of pastrami")

while "pastrami" in sandwich_orders:
    
    sandwich = sandwich_orders.pop()
    if sandwich == "pastrami":
        pass
    else:
        finished_sandwiches.append(sandwich)
        
print("\nThe following sandwiches are ready: \n")
for s in finished_sandwiches:
    print(s)
    