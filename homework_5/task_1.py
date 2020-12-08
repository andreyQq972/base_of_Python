with open("task_1_text.txt", "w") as f_obj:
    while True:
        content = input('Введите то, что хотите записать (просто Enter - выход):\n')
        f_obj.writelines(content)
        if not content:
            break
with open("task_1_text.txt") as f_obj:
    content_read = f_obj.readlines()
    print(content_read)
