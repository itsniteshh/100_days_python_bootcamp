# a function to check if the number is prime or not

num = int(input()) # enter a number from 1 to 100

def prime_checker(number):
    if num > 1:
        for i in range(2, num):
            
    # Iterate from 2 to n // 2
        
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
        


prime_checker(number= num)

