class user:
    """A class to store about user profile details from any social media page"""
    
    def __init__(self, first_name, last_name, user_id, age):
        """attributes about user profile"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
        self.login_attempt = 0
        
    def decribe_user(self):
        print(f"The users full name is {self.first_name} {self.last_name}")
        print(f"The users age is {self.age}")
        print(f"The users id is {self.user_id}")
        
    
    def greet_user(self):
        print(f"Welcome to the system, {self.first_name}")
        
    def increment_login(self):
        self.login_attempt += 1
        print(f"This is the {self.login_attempt} login attempt")
        
    
    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f"The login has been reset to {self.login_attempt}")
        

user1 = user("nitesh", "jha", "itsnitesh", 28)

user1.increment_login()