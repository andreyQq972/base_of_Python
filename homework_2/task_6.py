# Не удалось доделать в части сбора аналитики о товарах.

goods = int(input("Введите количество товаров: "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("Введите название товара: "), 'цена': input("Введите его цену: "),
                    'количество': input('Введите количество: '), 'eд': input("Введите единицу измерения: ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict({'название': my_dict.get('название'), 'цена': my_dict.get('цена'),
                      'количество': my_dict.get('количество'), 'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)