import usernam
bill = float (input("what's the total amount of the bill ? "))
per = int(input("what percentage would you like to give 10, 20, 70 etc... ? "))
num = int(input("The bill would be split among how many people? "))

#p = bill * per / 100
#print(round(p , 2))
k = bill / num
print(k)
s = k * per / 100
print(round(s , 2))