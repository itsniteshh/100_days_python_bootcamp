def cars(manufacturer, model_name, **functions):
    """car function to accept car details through kwags and returns dictionary"""
    
    functions["manufacturer"] = manufacturer
    functions["modelName"] = model_name
    
    return functions


car_details = cars("i3", "BMW", color = "Blue", type = "hybrid car")
print(car_details)