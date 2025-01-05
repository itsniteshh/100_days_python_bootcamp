'''
def vol(rad):
    """a function that computes the volume of a sphere given its radius"""
    # vol of spehre = 4/3µr3
    pi = 3.14
    
    volume = 4/3 * (pi * (rad**3))
    return volume

print(vol(2))


def ran_check(num, low, high):
    """a function that checks whether a number is in a given range(inc of high and low))"""
    final_num = 0
    for number in range(low, high+1):
        if num == number:
            final_num = num
    
    return final_num == num
    
    
print(ran_check(8, 2, 7))
    

def up_lows(s):
    """a function that accepts a string and calculates the number of upper case and lower case letters"""
    upper_counter = 0
    lower_counter = 0
    
    for alpha in s:
        if alpha.isupper():
            upper_counter += 1
        elif alpha.islower():
            lower_counter += 1
        else:
            pass
            
    return f"No. of upper case character: {upper_counter}\nNo. of lower case character: {lower_counter}"
print(up_lows("Hello Mr. Nitesh, how are you this fine Sunday?"))
            

def unique_list(lst):
    """A fucntion that takes a list and returns a new list with unique elements of the first list"""
    final_list = []
  
    for nums in lst:
        if nums in final_list:
            pass
        else:
            final_list.append(nums)
        
    return final_list
print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 2, 2, 5]))

def multiply(nums):
    """a function to multiply numbers"""
    total = 1
    
    for n in nums:
        
        total *= n
        
    return total
print(multiply([1, 2, 3, -4]))

def palindrome(s):
    """a palindrome is a word, phrase, or sequence that reads the same backward as forward."""
    new_word = s.replace(" ", "")
    return new_word[::-1]

print(palindrome("helleh helleh"))
'''
import string

alphabets = string.ascii_lowercase

def is_pangram(text):
    """a function to check whether a string is pangram or not. Pangram are words or sentences containing every letter of the alphabet atleast once"""
    final_alpha = []
    
    for i in text.lower().replace(" ", ""):
        if i in final_alpha:
            pass
        else:
            final_alpha += i
    
    final_alpha.sort()
    return final_alpha

print(is_pangram("The quick brown fox jumps over the lazy dog"))
