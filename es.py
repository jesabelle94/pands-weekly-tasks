# Write a program that reads in a text file and outputs the number of e's it contains
# The program should take the filename from an argument on the command line
# Author: Jenny Formentera

# I need to create a data/file which is moby-dick.txt / I searched 'moby-dick text csv' in Google and found https://www.gutenberg.org/files/2701/old/moby10b.txt
# This program will count and output how much 'e's' it contains within the csv 'moby-dick.txt' data file.


filename = "moby-dick.txt" # This line tells the program that we're going to read a file named "moby-dick.txt"

# This line creates a function called letterFrequency, the filename and the letter we're interested in (e)
def letterFrequency(filename, e):
    file = open(filename, 'r') # This line opens the file specified by the filename variable in read mode

    text = file.read() # This line reads the entire contents of the file into the variable text

    return text.count(e) # This line tells us how many times the letter "e" appears in the text we've read from the file

# # this code reads the contents of the file "moby-dick.txt" and counts how many times the letter 'e' appears in it. It then prints out this count.
print(letterFrequency('moby-dick.txt', 'e')) 

# Reference for the code: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/