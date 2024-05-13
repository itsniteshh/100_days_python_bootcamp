from art import logo, vs
import random
from game_data import data

end_of_game = True

def getting_data():
    """to get data from the list of dictionary """
    user_a= random.choice(data)
    
    # geeting follower
    name_a = user_a["name"]
    follower_count_a = user_a["follower_count"]
    description_a = user_a["description"]
    country_a = user_a["country"]
     
    return name_a, follower_count_a, description_a, country_a


        
    
    
    