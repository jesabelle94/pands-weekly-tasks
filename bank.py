# bank.py
# storing currency figures
# author: jenny formentera


number1 = float(input("Enter amount1 (in cent): "))
number2 = float(input("Enter amount2 (in cent): "))

num1 = number1 / 100  
num2 = number2 / 100

sum_of_numbers = num1 + num2
curr = "{:,.2f}".format(sum_of_numbers) 

print("The sum of these is €" + curr)
