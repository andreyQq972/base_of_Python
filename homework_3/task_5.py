def my_sum():
    sum_res = 0
    ex = False
    while not ex:
        number = input('Введите числа через пробел или нажмите Q для выхода: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Cумма ваших чисел = {sum_res}')
    print(f'Программа заверешна. Окончательная сумма = {sum_res}')


print(my_sum())
