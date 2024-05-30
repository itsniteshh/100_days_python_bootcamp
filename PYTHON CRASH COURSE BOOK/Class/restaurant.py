class restaurant:
    
    def __init__(self, restro_name, cuisine_type):
        
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restro_name} and it serves {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"The restaurant is open for dining") 
        
"""
my_restro = restaurant("nitesh", "chinese")
my_restro.describe_restaurant()
my_restro.open_restaurant()
"""