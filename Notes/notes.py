# normal access w/property decorator
class Rectangle:
    def __init__(self, width, height):
        # "_" before the attribute indicates that it is
        # private and can't be accessed outside of 
        self._width = width
        self._height = height


# begin "getter" methods: specifies the format when
# the values are called

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
# end "getter" methods    

# begin "setter" methods: define how to set (write) a
# value for an attribute

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be > 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print("Height must be > 0")

# end "setter" methods

# begin "deleter" methods:

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._width
        print("Height has been deleted")

rectangle = Rectangle(3, 4)


# still "works" but returns a warning that these are
# protected class members
print(rectangle.width) #3
print(rectangle.height) #4


del rectangle.width
# no longer works: there is no "._width" element for the
# rectangle object
print(rectangle.width) #3
