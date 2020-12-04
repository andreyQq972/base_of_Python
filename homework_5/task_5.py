try:
    with open("task_5_text.txt", "w+") as f_obj:
        content = input('Введите набор целых чисел, разделенных пробелами: ')
        f_obj.writelines(content)
        my_numb = content.split()
        print(f'Сумма введенных вами чисел: {sum(map(int, my_numb))}')
except ValueError:
    print('Ошибка: введено не число (не целое число).')
