from shape import Shape

class Triangle(Shape):
    def __init__(self, name, a, b, c):
        super().__init__(name, "Triangle")
        self.__a = a
        self.__b = b
        self.__c = c
    
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
    
    @property
    def area(self):
        p = (self.__a + self.__b + self.__c) / 2
        s = (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5
        return s
    
if __name__ == "__main__":
    triangle = Triangle("ABC", 3, 4, 5)
    print(triangle)  # Output: Triangle ABC area 6.0 m2