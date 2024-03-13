# weekly task 2
#bank.py
# storing currency figures
# author: Jenny Formentera


# prompts the user to input floating-point numbers

number1 = float(input("Enter amount1 (in cent): ")) 
number2 = float(input("Enter amount2 (in cent): "))

num1 = number1 / 100  # num1&2 is divided by 100 to convert from cents to euros
num2 = number2 / 100

sum_of_numbers = num1 + num2 # calculates the sum of the two amounts
curr = "{:,.2f}".format(sum_of_numbers)  #formats the sum of the numbers into euros

print("The sum of these is €" + curr)
