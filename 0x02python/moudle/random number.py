#password generator
#this program generates a 6 digits password for the user comprising of letters and numbers
import random
import string
import username

#ran_num = random.randord(2, 200)

#print(ran_num)
print(username)
# define the random module.
# #S = # number of characters in the string.
S = input("enter how many characters you want the password to be " )
#convert string to int
try:
    S = int(S)
    print("You entered:", S , "jh")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
#call random
ran = ''.join(random.choices(string.ascii_letters + string.digits, k = S))
print("your password is : " + str(ran))
# print the random data.

print("\t \nRemember to copy it out\n")
#for letter in range(ord('a'), ord('z') + 1):
    #print(chr(letter), end=' ')
    
    
    
#ran_alph = random.choice(letter)
#print(ran_alph)