#password generator
#this program generates a 6 digits password for the user comprising of letters and numbers

import string
import random

# Generate and print a random integer between 1 and 100 (inclusive)
#for _ in range(4):
#random_number = random.sample(range(1,100) ,4)
random_letter = random.sample(string.ascii_letters + string.digits, 5)

#print("Your generated number is: ", str(random_number)) #convert to string so it can be printed as an int


#print(random_number)
print(random_letter)