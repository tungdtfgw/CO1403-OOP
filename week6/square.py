from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)
        self.shape_type = "Square"



if __name__ == "__main__":
    square = Square("ABCD", 5)
    print(square)  # Output: Square ABCD area 25 m2