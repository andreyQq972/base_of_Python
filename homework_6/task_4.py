class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name}: {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} в городе: {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} больше разрешенной в городе! (60 км/ч)'


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name}: {self.speed} км/ч')
        if self.speed > 40:
            return f'Скорость {self.name} больше допустимой для рабочей машины! (40 км/ч)'


class PoliceCar(Car):
    pass


mercedes = TownCar(105, 'Черный', 'Мерседес', False)
volvo = WorkCar(47, 'Серый', 'Volvo', False)
print(volvo.turn_left())
print(f'Потом {volvo.turn_right()}, затем {volvo.stop()}')
print(volvo.go())
print(volvo.show_speed())
print(f'\n{mercedes.name} - {mercedes.color}')
print(mercedes.show_speed())
