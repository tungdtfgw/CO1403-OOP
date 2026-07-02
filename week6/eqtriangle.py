from isotriangle import IsoTriangle

class EquiTriangle(IsoTriangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)
        self.shape_type = 'Equilateral Triangle'


if __name__ == "__main__":
    t = EquiTriangle("ABC", 4)
    print(t)
    print(f'Side: {t.side}')