class user:
    """A class to store about user profile details from any social media page"""
    
    def __init__(self, first_name, last_name, user_id, age):
        """attributes about user profile"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
        
    def decribe_user(self):
        print(f"The users full name is {self.first_name} {self.last_name}")
        print(f"The users age is {self.age}")
        print(f"The users id is {self.user_id}")
        
    
    def greet_user(self):
        print(f"Welcome to the system, {self.first_name}")
    

user1 = user("nitesh", "jha", "itsnitesh", 28)
user1.decribe_user()
user1.greet_user()