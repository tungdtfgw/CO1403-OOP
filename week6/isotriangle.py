from triangle import Triangle

class IsoTriangle(Triangle):
    def __init__(self, name, base, side):
        super().__init__(name, base, side, side)
        self.shape_type = "Isosceles Triangle"

    @property
    def side(self):
        return self.b # or return self.c
    
    @property
    def base(self):
        return self.a
    
if __name__ == "__main__":
    t = IsoTriangle("ABC", 4, 6)
    print(t)
    print(f'Base: {t.base}')
    print(f'Side: {t.side}')