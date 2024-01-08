# import time
# import turtle
# import colorsys
# t = turtle.Turtle()
# start_time = time.time()
# s = turtle.Screen().bgcolor('black')
# t.speed(0)
# n = 70
# h = 0
# for i in range(360):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h+= 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for j in range(2):
#         t.left(2)
#         t.circle(100)
# stop_time = time.time()
# print(stop_time - start_time)
        
        
import turtle
turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(29)
squary.pencolor("red")
for i in range(400):
    squary.forward(i)
    squary.right(91)
    
squary.speed(29)
squary.pencolor("blue")
for i in range(400):
    squary.forward(i)
    squary.left(91)