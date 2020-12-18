from random import randint


def generate_unique_numbers(count, min_limit, max_limit):
    if count > max_limit - min_limit + 1:
        raise ValueError('Incorrect input parameters')
    nums = []
    while len(nums) < count:
        new = randint(min_limit, max_limit)
        if new not in nums:
            nums.append(new)
    return nums


class Barrel:

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)


class Card:

    def __init__(self):
        self.__rows = 3
        self.__cols = 9
        self.__nums_in_row = 5
        self.__data = None
        self.__empty_num = 0
        self.__crossed_num = -1
        uniques_count = self.__nums_in_row * self.__rows
        uniques = generate_unique_numbers(uniques_count, 1, 90)

        self.__data = []
        for i in range(0, self.__rows):
            tmp = sorted(uniques[self.__nums_in_row * i: self.__nums_in_row * (i + 1)])
            empty_nums_count = self.__cols - self.__nums_in_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self.__empty_num)
            self.__data += tmp

    def __str__(self):
        delimiter = '--------------------------'
        nums = delimiter + '\n'
        for index, num in enumerate(self.__data):
            if num == self.__empty_num:
                nums += '  '
            elif num == self.__crossed_num:
                nums += ' -'
            elif num < 10:
                nums += f' {str(num)}'
            else:
                nums += str(num)

            if (index + 1) % self.__cols == 0:
                nums += '\n'
            else:
                nums += ' '

        return nums + delimiter

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__crossed_num
                return
        raise ValueError(f'Number not in card: {num}')

    def closed(self) -> bool:
        return set(self.__data) == {self.__empty_num, self.__crossed_num}


class Game:

    def __init__(self):
        self.__num_barrels = 90
        self.__barrels = []
        self.__user_card = Card()
        self.__comp_card = Card()
        self.__barrels = generate_unique_numbers(self.__num_barrels, 1, 90)

    def play_round(self) -> int:
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - computer wins
        """

        barrel = self.__barrels.pop()
        print(f'Новый бочонок: {barrel} (осталось {len(self.__barrels)})')
        print(f'----- Ваша карточка ------\n{self.__user_card}')
        print(f'-- Карточка компьютера ---\n{self.__comp_card}')

        user_answer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if user_answer == 'y' and not barrel in self.__user_card or \
           user_answer != 'y' and barrel in self.__user_card:
            return 2

        if barrel in self.__user_card:
            self.__user_card.cross_num(barrel)
            if self.__user_card.closed():
                return 1
        if barrel in self.__comp_card:
            self.__comp_card.cross_num(barrel)
            if self.__comp_card.closed():
                return 2

        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('Игра окончена. Вы победили!')
            break
        elif score == 2:
            print('Игра окончена. Вы проиграли!')
            break
