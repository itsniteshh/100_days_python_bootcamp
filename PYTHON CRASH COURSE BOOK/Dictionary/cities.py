cities = {
    "mumbai": {
        "country": "India",
        "Population": "50cr",
        "known for": "financial capital"
        },
    "newyork": {
        "country": "america",
        "Population": "20cr",
        "known for": "coolest city"
        },
    "tokyo": {
        "country": "nepal",
        "Population": "20cr",
        "known for": "most advanced"
        },
}

for city, city_info in cities.items():
    print(f"City name: {city}")
    
    
    city_details = f"Country: {city_info["country"]}, Population: {city_info["Population"]}"
    fact = f"Known for: {city_info["known for"]}\n"
    
    print(city_details.capitalize())
    print(fact.capitalize())