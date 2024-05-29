

def user_profile(fname, lname, **userinfo):
    
    userinfo["first_name"] = fname
    userinfo["last_name"] = lname
    
    return userinfo

info = user_profile("nitesh", "jha", age = 28, location = "Mumbai")
print(info)