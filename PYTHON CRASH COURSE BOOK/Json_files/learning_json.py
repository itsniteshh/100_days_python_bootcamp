"""import json

nums = list(nums for nums in range(0, 20, 2))

file_name = "numbers.json"
with open(file_name, "w") as f:
    json.dump(nums, f)"""
    
    
import json
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)