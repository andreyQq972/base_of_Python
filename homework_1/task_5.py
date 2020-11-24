proceeds = int(input("Введите значение выручки вашей фирмы: "))
costs = int(input("Введите значение издержек вашей фирмы: "))
profit = proceeds - costs
paying = profit / proceeds
if proceeds > costs:
    print("Ваша фирма работает с прибылью. Рентабельность вашей фирмы составила: ", "%.2f%%" % (paying))
    members = int(input("Введите количество сотрудников вашей фирмы: "))
    profit_member = profit / members
    print("Прибыль фирмы в расчете на одного сотрудника составила: ", "%.0f" % (profit_member))
elif proceeds == costs:
    print("Ваша фирма вышла в ноль.")
else:
    print("Ваша фирма работает в убыток.")
