from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name, "Rectangle")

        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    # Override the area property from the Shape class
    @property
    def area(self):
        return self.__width * self.__height

if __name__ == "__main__":
    rect = Rectangle("ABCD", 5, 10)
    print(rect)  # Output: Rectangle ABCD area 50 m2