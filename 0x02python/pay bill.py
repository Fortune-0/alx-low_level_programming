#who's paying for the bill?
import random

bill = input("Enter your names seperated by a comma. ")
random_letter = random.choice(bill)
names = bill.split(", ")
print(names, ' you are paying the bills!')
print(random.choice(bill))
#print(names)
#!/usr/bin/python3
number = 98
print(f"{number} battery street")