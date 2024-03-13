# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Use The Newton method 

number = float(input("Enter a positive floating number: ")) # asks the user to input any positive floating-point number (decimal point numbers)

def sqrt(n): # this line stars a new function called sqrt to calculate the square root and n represent the number to want to calculate
    if n < 0:
        raise ValueError("Please enter a positive number") # if it gives a number < 0, it will prompt you to enter another number
    
    if n == 0:
        return 0 # if n is 0 it will inform that the sqrt of 0 is 0 
    
    x = n / 2  

    while True:
        root = (x + n / x) / 2 #inside this calculation, it will use the newton methon
        if abs(root - x) < 0.0001:
            return root
        x = root

print("The square root of", number, "is approximately", sqrt(number))

# I've used ChatGBT for assistance on this task.