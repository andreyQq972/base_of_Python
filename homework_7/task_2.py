from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @property
    @abstractmethod
    def tissue_square(self):
        pass

    @abstractmethod
    def _calc_tissue_square(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, measuring):
        self._measuring = measuring
        self._tissue_square = None
        self._clothes.append(self)

    def _calc_tissue_square(self):
        pass

    @property
    def tissue_square(self) -> float:
        if not self._tissue_square:
            self._calc_tissue_square()

        return self._tissue_square

    @property
    def measuring(self):
        return self._measuring

    @property
    def full_tissue_square(self):
        return sum([item.tissue_square for item in self._clothes])


class Coat(Clothes):
    def _calc_tissue_square(self):
        self._tissue_square = round(self.measuring / 6.5 + 0.5, 2)

    def __str__(self):
        return f"Для пальто {self.measuring} размера " \
               f"потребуется {self.tissue_square} кв. метров ткани"


class Suit(Clothes):
    def _calc_tissue_square(self):
        self._tissue_square = round(2 * self.measuring * 0.01 + 0.3, 2)

    def __str__(self):
        return f"Для костюма на рост {self.measuring} см. " \
               f"потребуется {self.tissue_square} кв. метров ткани"


coat = Coat(48)
print(coat)
suit = Suit(180)
print(suit)
print(f'Общий расход ткани: {coat.full_tissue_square} кв. метров')
print(f'Общий расход ткани: {suit.full_tissue_square} кв. метров')
