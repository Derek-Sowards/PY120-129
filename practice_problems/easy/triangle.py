class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def area(self):
        return self._height * self._width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)




square = Square(5)
print(square.area == 25)      # True




rect = Rectangle(4, 5)
print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True