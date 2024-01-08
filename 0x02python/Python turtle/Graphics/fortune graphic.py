# # import turtle

# # # Create a turtle screen and turtle object
# # screen = turtle.Screen()
# # fortune_turtle = turtle.Turtle()

# # # Function to draw the word "Fortune"
# # def draw_fortune():
# #     # F
# #     fortune_turtle.forward(50)
# #     fortune_turtle.left(90)
# #     fortune_turtle.forward(20)
# #     fortune_turtle.backward(20)
# #     fortune_turtle.right(90)
# #     fortune_turtle.forward(50)
# #     fortune_turtle.penup()

# #     # Move to draw the letter "O"
# #     fortune_turtle.forward(20)
# #     fortune_turtle.pendown()

# #     # O
# #     fortune_turtle.circle(25)

# #     # Move to draw the letter "R"
# #     fortune_turtle.penup()
# #     fortune_turtle.left(90)
# #     fortune_turtle.forward(10)
# #     fortune_turtle.pendown()

# #     # R
# #     fortune_turtle.forward(40)
# #     fortune_turtle.backward(40)
# #     fortune_turtle.right(90)
# #     fortune_turtle.forward(25)
# #     fortune_turtle.left(90)
# #     fortune_turtle.forward(20)
# #     fortune_turtle.penup()

# #     # Move to draw the letter "T"
# #     fortune_turtle.backward(10)
# #     fortune_turtle.left(90)
# #     fortune_turtle.forward(10)
# #     fortune_turtle.pendown()

# #     # T
# #     fortune_turtle.forward(50)
# #     fortune_turtle.backward(25)
# #     fortune_turtle.right(90)
# #     fortune_turtle.forward(50)
# #     fortune_turtle.penup()

# # # Draw the word "Fortune"
# # draw_fortune()

# # # Close the turtle graphics window when clicked
# # screen.exitonclick()
# import turtle

# # Set up the turtle screen
# screen = turtle.Screen()
# screen.bgcolor("white")

# # Create a turtle object
# name_turtle = turtle.Turtle()
# name_turtle.speed(2)  # Set turtle speed (1=slowest, 10=fastest)

# # Function to draw a letter
# def draw_letter(letter, font_size):
#     name_turtle.write(letter, font=("cour", font_size, "normal"))
#     name_turtle.forward(10)  # Add some space between letters

# # Function to draw a name
# def draw_name(name):
#     for letter in name:
#         draw_letter(letter, 36)

# # Move the turtle to the starting position
# name_turtle.penup()
# name_turtle.goto(-100, 0)
# name_turtle.pendown()

# # Draw the name "Fortune"
# draw_name("Fortune")

# # Close the turtle graphics window when clicked
# screen.exitonclick()

import turtle as t
t.pen()
t.bgcolor("black")
colors=["red","green","yellow","blue","gray","purple","aqua","brown"]
name=t.textinput("Cyberpunk",
"Cyberpunk")
s=int(t.numinput("Number of sides",
"How many sides you want(1-20)",10,1,20))
for i in range(100):
    t.pencolor(colors[i%s%5])
    t.penup()
    t.forward(i*5)
    t.pendown()
    t.write(name,font=("",
    int((i*2+4)/4),"bold"))
    t.left(360/s+4)