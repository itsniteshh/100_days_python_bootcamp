# there are two variables a and b, we need to swap them

a = int(input("enter any num: "))
b = int(input("enter any num: 5"))

# storing value of a in c for temp swap
c = a

a = b
b = c

print(f"a = {a}")
print(f"b = {b}")

