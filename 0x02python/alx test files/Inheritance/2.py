# def is_same_class(obj, a_class):
#     return type(obj) is a_class

class BaseGeometry:
    def area(self):
        def integer_validator(self, name, value):
            self.name = name
            self.value = value
            
            if not (isinstance(value, int)):
                raise TypeError("{} must be an integer".format(name))
            if not (isinstance(0 <= value)):
                raise TypeError("{} must be an integer".format(name))

            raise Exception("area not implemented")