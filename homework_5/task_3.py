with open("task_3_text.txt") as f_obj:
    content = f_obj.read()
    print(f'Сотрудники фирмы и их оклад: \n{content}')
    f_obj.seek(0)
    sal = []
    poor = []
    my_list = f_obj.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад менее 20 тыс. имеют следующие сотрудники: {poor},\n'
      f'Средний оклад сотрудников: {sum(map(float, sal)) / len(sal)}')
