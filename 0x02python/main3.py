# Square = __import__('test').square

# my_square_1 = Square(3)
# print("Area: {}".format(my_square_1.area()))

# try:
#     print(my_square_1.size)
# except Exception as e:
#     print(e)

# try:
#     print(my_square_1.__size)
# except Exception as e:
#     print(e)

# my_square_2 = Square(5)
# print("Area: {}".format(my_square_2.area()))

"""5 main.py"""
Square = __import__('test').square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")