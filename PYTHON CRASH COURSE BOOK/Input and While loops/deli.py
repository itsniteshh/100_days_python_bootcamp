sandwich_orders = ["chicken", "mushroom", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    
    sandwich_cooking = sandwich_orders.pop()
    print(f"We are currently cooking {sandwich_cooking}")
    
    finished_sandwiches.append(sandwich_cooking)


print("The following sandwiches are ready:\n")
for sandwich in finished_sandwiches:
    print(sandwich)
