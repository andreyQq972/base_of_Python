class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        try:
            matrix = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
            for i in range(len(self.my_list)):
                for j in range(len(other.my_list[i])):
                    matrix[i][j] = self.my_list[i][j] + other.my_list[i][j]
            return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))
        except IndexError:
            print('Можно складывать только одинаковые по размеру матрицы!')

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.my_list]))


my_matrix_1 = Matrix([[7, 2, 27],
                      [5, 43, 11],
                      [21, 35, 66]])
my_matrix_2 = Matrix([[57, 81, 17],
                      [90, 25, 43],
                      [22, 7, 21]])
print(f'Матрица №1:\n{my_matrix_1}\n')
print(f'Матрица №2:\n{my_matrix_2}\n')
print(f'Результат сложения этих двух матриц:\n{my_matrix_1 + my_matrix_2}')
