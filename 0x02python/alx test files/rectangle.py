class rectangle:
    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value <0:
            raise ValueError('height must be >= 0')
        
    # def __init__(self, width=0, height=0):
    #     self._width = width
    #     self._height = height
    
    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.breadth
    
    def perimeter(self):
        """Retuns the perimeter of the rectangle."""
        #
        if self.__lenght == 0 or self.__width == 0:
          #  return 0
         return 2 * (self.__lenght + self.__width)