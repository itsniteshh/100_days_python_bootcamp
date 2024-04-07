country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string


travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(c, v, l):
    
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["list_of_cities"] = list_of_cities
    
    
    travel_log.append(new_country)
  
  

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)

print(travel_log)
