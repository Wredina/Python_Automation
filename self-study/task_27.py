# Напишите функцию для транспонирования матрицы

def transpon(matrix: list[int]) -> list[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    print(rows)
    print(cols)

    # Создаем новую матрицу, чтобы хранить результат транспонирования
    transposed_matrix = []

    # Проходим по столбцам исходной матрицы
    for j in range(cols):
        # Создаем временную строку для хранения столбца
        temp_row = []
        # Проходим по строкам исходной матрицы и добавляем элементы во временную строку
        for i in range(rows):
            temp_row.append(matrix[i][j])
        # Добавляем временную строку в транспонированную матрицу
        transposed_matrix.append(temp_row)

    return transposed_matrix


matrix = [[1, 2, 3],
          [4, 5, 6]
          ]

print(transpon(matrix))
