my_list = input("Введите несколько слов, разделенных пробелами: ").split()
i = 0
for el in my_list:
    i +=1
    if len(str(my_list)) <= 10:
        print(f" {i}: {el}")
    else:
        print(f" {i}: {el [0:10]}")
