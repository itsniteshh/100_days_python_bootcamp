friends = ["Nitesh", "Aman", "Arjun", "Ganesh", "Pro"]

import random

random_num = random.randint(1, len(friends))-1
bill_payer = friends[random_num]

# or random.choice

print(f"{bill_payer} is gonna pay everyone's bill today")