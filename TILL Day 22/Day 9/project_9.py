from art import logo

print(logo)
print("Welcome to the Secret Auction Program")

end_of_game = True

bidder_details = {}
highest_bid = 0
highest_bidder = ""

while end_of_game:
    #while loop to continue looping till the game continues 
        
    name = input("Name: ") #enter your first name
    bid_amount = int(input("Bid amount: ")) #to save bid amount
    
    bidder_details[name] = bid_amount
    
    game_time = input("Would you like to continue? ").lower() #to check if the user wants to continue 
    
    # for looping through the dict and using logicals
    for k, v in bidder_details.items():
        
        if v > highest_bid:
            highest_bid = v
            highest_bidder = k


    if game_time == "no": 
        end_of_game = False
    else:
        print(bidder_details)
        
print(f"Highest bidder is {highest_bidder}, with {highest_bid} bid.")
    

    
    
    

    
    
        
    