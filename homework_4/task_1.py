from sys import argv

script_name, output, rate, bonus = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", output)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
print(f'Итог расчета по формуле: (выработка в часах*ставка в час) + премия: {int(output) * int(rate) + int(bonus)}')
