num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open("task_4_text.txt") as f_obj:
    content = f_obj.read()
    print(f'Изначальное содержимое: \n{content}')
    f_obj.seek(0)
    for i in f_obj:
        i = i.split(' ', 1)
        new_file.append(num[i[0]] + '  ' + i[1])
    print(f'Содержимое для нового файла: {new_file} успешно записано в файл task_4_text_new.txt')

with open('task_4_text_new.txt', 'w') as f_obj_2:
    f_obj_2.writelines(new_file)
