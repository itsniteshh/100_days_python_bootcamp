from restaurant import restaurant

class IceCreamStand(restaurant):
    
    def __init__(self, restro_name, cuisine_type):
        super().__init__(restro_name, cuisine_type)
        
        self.flavor = ["chocolate", "vanilla", "honey", "dark choco"]
        
    
    def show_desert(self):
        print("We have following flavor ice cream in the market: ")
        for flav in self.flavor:
            print(flav)
            
            
ice_cream = IceCreamStand("nitesh", "chinese")
ice_cream.show_desert()

