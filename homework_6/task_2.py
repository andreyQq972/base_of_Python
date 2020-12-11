class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_asphalt(self):
        height_cm = 5
        mass_kg = 25
        print(f'{int((self._length * self._width *  height_cm * mass_kg) / 1000)} т')


road_bed = Road(20, 5000)
road_bed.mass_asphalt()
