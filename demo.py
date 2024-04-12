MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 600,
    "milk": 400,
    "coffee": 100,
    "money": 0
}



end_of_game = True

# TO DO 4- CHECK RESOURCES SUFFICEINT        
def resource_sufficient(want, resources, MENU):
    
    if resources["coffee"] >= MENU[want]["ingredients"]["coffee"]:
        if resources["water"] >= MENU[want]["ingredients"]["water"]:
            if want == "espresso":
                pass
            else:
                if resources["coffee"] >= MENU[want]["ingredients"]["coffee"]:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
                

#ToDo 5-  PROCESS COINS        
def processing_money(five, ten, twenty, hundred):
    
    total_five = five * 5
    total_ten = ten * 10
    total_twenty = twenty * 20
    total_hundred = hundred * 100
    
    total = total_five + total_ten + total_twenty + total_hundred
    return total
 # ToDo 6 - CHECK TRANSACTION SUCCESSFUL     
 
def successful_transaction(total_amount, want, resources):
    
    if total_amount >= MENU[want]["cost"]:
        excess_amt = total_amount - MENU[want]["cost"]
        resources["money"] = total_amount - MENU[want]["cost"]
        print(f"Here is {excess_amt} in change.")
        
        return True
    else:
        return False
    
    
# ToDo 7 - MAKE COFFEE    
def make_coffee(want, transaction, resources, menu):
    
    if successful_transaction(total_amount, want, resources):
        resources["money"] += MENU[want]["cost"]
        resources["water"] -= MENU[want]["ingredients"]["water"]
        resources["coffee"] -= MENU[want]["ingredients"]["coffee"]
        if want == "espresso":
            pass
        else:
            resources["milk"] -= MENU[want]["ingredients"]["milk"]               
  
        
# ToDo 1 - PROMPT USER BY ASKING WHAT WOULD YOU LIKE

while end_of_game:
    want = input("what would you like? (espresso/latte/cappuccino): ")
        
# to do 2 - TURN OFF THE COFFEE MACHINE BY ENTERING OFF    
    
    if want == "off":
        end_of_game = False    
        
# TO DO 3 - PRINT REPORT
    elif want == "report":
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: {resources["money"]}")
    
    else:
        if resource_sufficient(want, resources, MENU):
            print("Please insert coins.")
            five_rupees = int(input("How many 5s? "))
            ten_rupees = int(input("How many 10s? "))
            twenty_rupees = int(input("How many 20s? "))
            hundred_rupees = int(input("How many 100s? "))
            total_amount = processing_money(five_rupees, ten_rupees, twenty_rupees, hundred_rupees)
            
            if successful_transaction(total_amount, want, resources):
                make_coffee(want, successful_transaction, resources, MENU)
                print(f"Here is a {want}🍵 for you")
            else:
                end_of_game = False
        else:
            #print("Sorry there is not enough water")
            end_of_game = False
    
    
