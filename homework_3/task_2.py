def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name='Иван', surname='Иванов', year='1950', city='Москва', email='ivanov@mail.ru',
              telephone='8-999-777-05-77'))
