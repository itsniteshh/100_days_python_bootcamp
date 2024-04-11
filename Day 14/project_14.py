from art import logo, vs
import random
from game_data import data

def getting_data_a():
    """to get data from the list of dictionary """
    user_a= random.choice(data)
    
    # geeting follower
    name_a = user_a["name"]
    follower_count_a = user_a["follower_count"]
    description_a = user_a["description"]
    country_a = user_a["country"]
     
    return name_a, follower_count_a, description_a, country_a

def getting_data_b():
    """to get data from the list of dictionary """
    user_b= random.choice(data)
    
    #getting follower data
    name_b = user_b["name"]
    follower_count_b = user_b["follower_count"]
    description_b = user_b["description"]
    country_b = user_b["country"]
    
    return name_b, follower_count_b, description_b, country_b

end_of_game = True
score = 0

user_name_a, user_follower_a, user_desc_a, user_country_a = getting_data_a()
user_name_b, user_follower_b, user_desc_b, user_country_b = getting_data_b()
    
compare_a = f"Compare A: {user_name_a}, a {user_desc_a}, from {user_country_a}"
compare_b = f"Against B: {user_name_b}, a {user_desc_b}, from {user_country_b}"

while end_of_game:
    
    print(logo)
    print(compare_a)
    print(vs)
    print(compare_b)
    
    followers = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    

    
    
    if user_follower_a > user_follower_b:
        score += 1
        compare_a = compare_b
        
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_of_game = False
    
    
    
        
    
    
    