#!/usr/bin/python
import time
from random import choice



print('Helps user decide on what to EAT')

#animes = ['game', 'voltron', 'cyberpunk']

#print(choice(animes))

my_list = []  # Create an empty list

# Prompt the user for input
while True:
    user_input = input("Enter a FOOD (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break  # Exit the loop if the user enters 'q'
    my_list.append(user_input)  # Add the input to the list

# Print the resulting list
print("Your list:", my_list)

print(choice(my_list))

time.sleep(20)
