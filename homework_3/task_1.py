def my_division():
    try:
        var_1 = int(input("Введите первое число - делимое: "))
        var_2 = int(input("Введите второе число - делитель: "))
        res = var_1 / var_2
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    except ValueError:
        return 'Введено не число'
    return res


print("Результат деления:", my_division())
