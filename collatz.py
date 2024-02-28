# Write a program that asks the user to input any positive integer and 
# outputs the successive values of the following calculation. 
# Have the program end if the current value is one.

# 10 5 16 8 4 2 1

n = int(input("Enter a positive integer: ")) # asks the user to input any positive integer

while n != 1:
    if n % 2 == 0: # if number is even, divide it by two 
        n  = n/2 
    else: 
        n = 3*n + 1  # if number is odd, multiply it by three and add one - rule of collatz
    
    print (n)


# reference: https://www.youtube.com/watch?v=XHXCs2ZLRIY