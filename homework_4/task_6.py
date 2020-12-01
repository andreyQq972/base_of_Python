from itertools import count, cycle
print('Вывод целых чисел с 3 до 10:')
for el in count(3):
    if el > 10:
        break
    else:
        print(el)
print('Повтор элементов списка [1, 2, 3]:')
number_end = 0
for el in cycle("123"):
    if number_end > 11:
        break
    print(el)
    number_end += 1
