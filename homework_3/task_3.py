def my_max_sum():
    var_1 = int(input("Введите первое число: "))
    var_2 = int(input("Введите второе число: "))
    var_3 = int(input("Введите третье число: "))
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    elif var_2 <= var_1 <= var_3 or (var_1 >= var_2 and var_2 <= var_3):
        return var_1 + var_3
    else:
        return var_2 + var_3


print('Результат суммы наибольших двух аргументов:', my_max_sum())
