from users import user

class Admin(user):
    
    """def __init__(self,first_name, last_name, user_id, age):
        super().__init__(self, first_name, last_name, user_id, age)"""
        
    def __init__(self, first_name, last_name, user_id, age):
        super().__init__(first_name, last_name, user_id, age)
        
        self.privileges = ["can add post", "can delete post", "can be user"]
        
        
    def show_privileges(self):
        print("The following privileges are available to you as admin: ")
        for priv in self.privileges:
            print(priv)
            
admin_access = Admin("nitesh", "jha", "itsnitesh", 28)
admin_access.show_privileges()
