my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг: {my_list}")
numb = int(input("Введите целое число для добавления в рейтинг: "))
for el in range(len(my_list)):
    if my_list[el] == numb:
        my_list.insert(el + 1, numb)
        break
    elif my_list[0] < numb:
            my_list.insert(0, numb)
    elif my_list[-1] > numb:
            my_list.append(numb)
    elif my_list[el] > numb and my_list[el + 1] < numb:
            my_list.insert(el + 1, numb)
print(f"Новый рейтинг: {my_list}")