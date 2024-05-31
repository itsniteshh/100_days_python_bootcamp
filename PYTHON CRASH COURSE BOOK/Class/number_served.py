class restaurant:
    
    def __init__(self, restro_name, cuisine_type):
        
        self.restro_name = restro_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restro_name} and it serves {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"The restaurant is open for dining") 
        
    def customers_served(self):
        print(f"The restaurant {self.restro_name} has served {self.number_served} customers")
        
    def increment_number_served(self, increment_num):
        if increment_num > self.number_served:
            self.number_served = increment_num
        else:
            pass
        
        
myrestro = restaurant("Nitesh", "chinese")
myrestro.increment_number_served(29)
myrestro.customers_served()
