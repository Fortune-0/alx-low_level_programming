class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def display(self):
        for _ in range(self.height):
            print('#' * self.width)
            
        r = Rectangle(5, 3)
        r.display()
