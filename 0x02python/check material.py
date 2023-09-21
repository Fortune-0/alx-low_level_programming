# The carbon content of steel is <= 2.14%, while for cast iron it is =2.14 >= 6.67%
print("check if the material is \"CAST-IRON\" OR \"STEEL\"" )
a = float(input("enter the carbon content of the material "))
#b = float(input("enter the carbon content of the material "))
if (a > 0 and a <= 2.14):
    print("The material is steel")
elif (a >= 2.14 and a <= 6.67):
    print("The material is Cast Iron")
elif (a > 6.68):
    print("The material is not metal")
    
