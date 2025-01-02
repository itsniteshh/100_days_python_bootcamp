# Warm-up problems
'''
def lesser_of_two_evens(a, b):
    """print lesser of the two numbers based on even or odd"""    
    if (a % 2 == 0) and (b % 2 == 0):
        return min (a, b)
    
    else:
        return max (a, b)
        
print(lesser_of_two_evens(11, 21))


def animal_crackers(text):
    """function that takes a two word string and return true if both words begin with same letter"""
    word = text.split(" ")
    
    return word[0][0].lower() == word[1][0].lower()
    
print(animal_crackers("n n"))


def makes_twenty(n1, n2):
    """given two int, return true if sum is 20 or if one of the int is 20. Else True"""
    return n1 == 20 or n2 == 20 or n1 + n2 == 20
    
print(makes_twenty(10, 10))

# Level 1 PROBLEMS
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


def almost_there(n):
    """given an integer n, return True if n is within 10 of either 100 or 200"""
    lowest = 0
    if n > 100: # checking to see if n is greater than 100, if yes - We % by 100 to get lowest remainder
        lowest = n % 100
    else: # if n is less than 100, we subtract it from 100 directly
        lowest = 100 - n
        
    return lowest <= 10 #checking if the above conidtion value is less than 10
        
print(almost_there(209))


# Level 2 programs

def find_33(nums):
    """Given an araay, find if there exists a 3 next to a 3"""
    
    for num in range(len(nums)-1):
        if nums[num] == nums[num + 1]:
            return True 
    else:
        return False
            
print(find_33([1, 3, 32, 3]))


def paper_doll(text):
    """given a string, return a string where for every char in original there are 3 char"""
    split_word = []
    
    for words in text:
        words *= 3
        split_word.append(words)
    
    return "".join(split_word)
        
print(paper_doll("Mississippi"))


def black_jack(a, b, c):
    """given 3 integers between 1 and 11, if their sum is less than or equal to 21, returns their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum(even after adjustment) exceeds 21, return 'BUST'"""
    total_sum = (a+b+c)
    
    if total_sum <= 21:
        return total_sum
    
    elif (total_sum > 21) and (a == 11 or b == 11 or c == 11):
        total_sum -= 10
    
    if total_sum > 21:
        return "BUST"
    else:
        return total_sum
    
print(black_jack(9, 9, 11))
'''

def summer_69(arr):
    """return the sum of numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 if no numbers"""
    
    if
    
print(summer_69([1, 3, 5]))