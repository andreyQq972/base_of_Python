from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self, __color):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        iterator = cycle(self.__color)
        while i < 6:
            print(next(iterator))
            if i == 0 or i == 3:
                sleep(7)
            elif i == 1 or i == 4:
                sleep(5)
            elif i == 2 or i == 5:
                sleep(2)
            i += 1


tr_light = TrafficLight('Красный')
tr_light.running()
