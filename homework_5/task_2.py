with open("task_2_text.txt") as f_obj:
    content = f_obj.read()
    print(f'Содержимое файла: \n{content}')
    f_obj.seek(0)
    content = f_obj.readlines()
    print(f'Количество строк в файле: {len(content)}')
    f_obj.seek(0)
    n = 1
    for content in f_obj:
        content = content.split()
        print(f'Количество слов в {n}-й строке: {len(content)}')
        n += 1
