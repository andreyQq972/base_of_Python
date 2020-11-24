time = int(input("Введите количество секунд и мы переведем их в формат чч:мм:сс: "))
time_hours = time // 3600
time_minutes = (time % 3600) // 60
time_seconds = ((time % 3600) % 60)
# print(f"{time_hours}:{time_minutes}:{time_seconds}")
if time < 360000:
    print ("%02i:%02i:%02i" % (time_hours, time_minutes, time_seconds))
else:
    print ("Для формата чч:мм:сс есть ограничение в 360 000 секунд. Попробуйте заново.")