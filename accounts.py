# Weekly Task 03
# Please enter a 10 digit account number: 1234567890 and replace the first 6 digits with Xs and show only the last 4 digits)
# Author: Jenny Formentera


accountno = input("Please enter a 10 digit account number:")
print("XXXXXX"+accountno[6:10])

'''
# modify the program to deal with account numbers of any length

accountno = input("Please enter an account number:")
print(accountno[0:4]) #prints the last 4 digits of the account number
'''