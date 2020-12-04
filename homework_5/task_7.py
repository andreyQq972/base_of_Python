import json
profit, pr = {}, {}
prof, prof_aver, i = 0, 0, 0
with open('task_7_text.txt') as f_obj:
    content = f_obj.read()
    print(f'Данные о фирмах:\n{content}')
    f_obj.seek(0)
    for line in f_obj:
        name, firm, proceeds, costs = line.split()
        profit[name] = int(proceeds) - int(costs)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
    else:
        print(f'Средняя прибыль отсутсвует. Все работают в убыток')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании: {profit}')

with open('task_7_text_for_js.json', 'w') as write_json:
    json.dump(profit, write_json)
    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n{js_str}')
