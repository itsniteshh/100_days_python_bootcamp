food_menu = ("panner chilly", "veg thali", "manchurian", "panner paratha", "chinese")

print(f"Ready to serve foods are: ")
for items in food_menu:
    print(items)
    
food_menu[0] = "idli vada"
print(food_menu)