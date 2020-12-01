x = 5
y = -3


def my_func(x, y):
    res = x ** y
    return res


print('Решение первым способом:', x, '^', y, '=', my_func(x, y))


def my_func_new(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print('Решение вторым способом:', x, '^', y, '=', my_func_new(x, y))
