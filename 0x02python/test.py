# print('Hello world')
#a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
#a.get('projects')
#print(a.__getstate__)

#a = [2, 3, 4, 5,]

#a [2] = 10
#b = a
#print(b)
#print(a)


#def common_elements(set_1, set_2):
        #set_1 = [1, 4, 3, 8]
        #set_2 = [2, 0, 3, 4]
        #return set_1 & set_2
#print("Common elements are in both sets")
    #else:
      #  print("No common element found between the two sets")

# #import random
# #number = random.randint(-10, 20)
# #if number > 0:
#     #print(f"{number:d} is positive")
# #elif number == 0:
#     #print(f"{number:d} is zero")
# #else:
#     #print(f"{number:d} is negative")
    
# class square:
#     def __init__(self, size=0):
#         def check_integer(side):
            
#             @property
#             def side(self):
#                 return self._side
#         @side.setter
#         def side(self, value):
#             if not isinstance(size, int):
#                 raise TypeError('Only integers are allowed')
#             elif side <0:
#                 raise ValueError('size must be >= 0')
#             elif print(f"{size} is an integer and it's greater than zero."):
#                 return size
#             else:
#                 self.__size = side
#             #def __init__(self, size=0):
#                 #defines area function
#                 def area(self):
#                 #returns area
#                     return self.__size ** 2
#                 def my_print(self):
#                     if size.self == 0:
#                         print("Square is not created")
#                     else:
#                         for i in range (self.__size):
#                             for j in range (self.__size):
#                                 print("#", end="")
#                                 print()
        
class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(u.id)
print(User.id)