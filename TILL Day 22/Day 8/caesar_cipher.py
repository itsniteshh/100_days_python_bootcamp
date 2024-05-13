alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 26


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def cipher(t, s, d):
    
    # declaring list to store msg
    new_msg = []
    
    # Todo 3 - for looping through the text
    for t in text:
        
        if  " " in text:
            pass
        new_position = alphabet.index(t) #finding out the index of the alphabete
        
        if d == "encode":
            new_position += shift
        else:
            new_position -= shift
        
        new_msg += alphabet[new_position]
    

    final_msg = ("".join(new_msg))
    print(final_msg)    
        
    
    
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
cipher(t = text, s = shift, d= direction)