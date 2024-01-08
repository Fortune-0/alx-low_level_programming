# Password generator
#This program generates a n digits password for the user comprising of letters and numbers
#!/usr/bin/env python3


# define the random module.
import random
import string
import username

#Asks the user for his/her name
print(username)

#"use" this ask the user the purpose or site for the password
use = input("What site or application is this password for? ")
#S = # number of characters in the string.
S = input("Enter how many characters you want the password to be " )

try:
    #convert string to int
    S = int(S)
    print("You entered:", S , "")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    
#calls random module to generate both string and integer
password = ''.join(random.choices(string.ascii_letters + string.digits, k = S))
#print("your password is : " + str(password))
# print the random data.

#saving the password to a file name "Saved.txt"

with open('Saved.txt', 'a+') as f:
    f.write(str('\n'))
with open('Saved.txt', 'a+') as f:
    f.write(str(use) + ' ')
    
with open('Saved.txt', 'a+') as f:
    f.write(str(password))
    
#with open('Password.txt', 'a') as f:
#    f.write(str('\n'))
    
#with open('Password.txt', 'a') as f:
 #   f.write(str(password))

#prints the password to the screen
print(f"The generated password '{password}' has been saved to Saved.txt")

print("\t \nRemember to copy it out though\n")

