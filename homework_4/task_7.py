from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


number = int(input('Введите число, факториалы от 1 до которого вы хотите узнать: '))

fact = fact()
x = 1
for i in fact:
    if x < number:
        print(f'Факториал {x}! = {i}')
        x += 1
    else:
        break
