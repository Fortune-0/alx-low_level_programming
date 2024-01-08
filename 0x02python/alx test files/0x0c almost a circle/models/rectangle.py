from base import Base

class Rectangle (Base):
    def __init__(self, width, height, area, x=0, y=0, id=None):
        super().__init__()
        self.width = width
        self.height = height
        self.area = area
        self.x = x
        self.y = y
        
        @property
        def width(self):
            return self.__width
        
        @width.setter
        def width(self, value):
            if value <= 0:
                raise ValueError("Width must be > 0")
            self.__width = value
            
        @property
        def x(self):
            return self.__x
        
        @x.setter
        def x(self, value):
            if value <= 0:
                raise ValueError("Width must be > 0")
            self.__x = value
            
        @property
        def y(self):
            return self.__y
        
        @y.setter
        def y(self, value):
            if value <= 0:
                raise ValueError("Width must be > 0")
            self.__y = value
        
        @property
        def area(self):
            return self.height * self.width
        
        #def display (self):
            
    def display(self):
        for _ in range(self.height):
            print('#' * self.width)

        
        def update(self, *args, **kwargs):
            if args is not None and len(args) is not 0:
                list_atrr = ['id', 'width', 'height', 'x', 'y']
                for i in range(len(args)):
                    setattr(self, list_atrr[i], args[i])
                else:
                    for key, value in kwargs.items():
                        setattr(self, key, value)
                    
            