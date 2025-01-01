
'''
def lesser_of_two_evens(a, b):
    """print lesser of the two numbers based on even or odd"""    
    if (a % 2 == 0) and (b % 2 == 0):
        if a > b:
            return b
        else:
            return a
    
    else:
        if a > b:
            return a
        else:
            return b
        
print(lesser_of_two_evens(11, 21))


def animal_crackers(text):
    """function that takes a two word string and return true if both words begin with same letter"""
    word = text.split(" ")
    
    return word[0][0].lower() == word[1][0].lower()
    
print(animal_crackers("n n"))


def makes_twenty(n1, n2):
    """given two int, return true if sum is 20 or if one of the int is 20. Else True"""
    if n1 == 20 or n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    
print(makes_twenty(10, 10))


def old_macdonald(name):
    """capitalize first and fourth letter of a name"""
    new_name = ""
    
    letter_1 = name[0].upper()
    mid_letter = name[1:3]
    letter_4 = name[3].upper()
    rest_letter = name[4:]
    
    new_name = letter_1 + mid_letter + letter_4 + rest_letter
    return new_name

print(old_macdonald("macdonald"))


def master_yoda(text):
    """Given a string, reverse it entirely"""
    
    new_list = text.split(" ")
    final_list = new_list[::-1]
    final = " ".join(final_list)
    
    return final

print(master_yoda("I am Nitesh"))
'''

