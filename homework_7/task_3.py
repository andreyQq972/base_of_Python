class Cell:
    def __init__(self, count: int):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cell(self.count - other.count)
        print(f"{self.count} - {other.count}: Вычитание невозможно.")

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def __str__(self) -> str:
        return f"Клетка состоит из {self.count} ячеек"


c1 = Cell(23)
print('1-я', c1)
c2 = Cell(11)
print('2-я', c2)
print('Результат сложения двух клеток: ', c1 + c2)
print('Результат вычитания двух клеток: ', c1 - c2)
print('Результат вычитания двух клеток наоборот: ', c2 - c1)
print('Результат умножения двух клеток: ', c1 * c2)
print('Результат целочисленного деления двух клеток: ', c1 / c2)
