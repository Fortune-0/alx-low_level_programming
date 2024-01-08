import turtle
import random

fort = turtle
# squa = turtle'
colours = ["red", "blue", "green", "purple", "indigo"]
# # print the F word

# fort.color('blue')
fort.bgcolor(random.choice(colours))
# fort.back(80)
# fort.down()
# fort.left(90)
# fort.back(50)
# fort.left(90)
# fort.back(50)
# fort.forward(50)
# fort.left(90)
# fort.down()
# fort.forward(70)

# # print a square
# for _ in range(4):
#     squa.forward(100)
#     squa.left(90)

def shape(sides):
    for _ in range (sides):
        angle = 360 / sides
        fort.forward(100)
        fort.left(angle)
        
for shape_side in range(3, 10):
    shape(shape_side)
        
fort.exitonclick()
# exit turtle when a key of screen is clicked