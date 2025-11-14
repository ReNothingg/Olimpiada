# 1. Читаем N
n = int(input())

# 2. Создаем пустой список для матрицы
matrix = []

# 3. Запускаем цикл N раз, чтобы прочитать n строк
for i in range(n):
    # Читаем одну строку как список чисел (например, [1, 2, 3])
    row = list(map(int, input().split()))
    # Добавляем (append) эту строку в нашу матрицу
    matrix.append(row)

# 4. Читаем r, c, k (например, 1 2 2)
r, c, k = map(int, input().split())

# 5. Переводим "человеческие" индексы (с 1)
#    в "питоновские" (с 0)
r = r - 1
c = c - 1

# 6. Создаем пустой список для временной копии
temp_square = []

# 7. Вложенные циклы (k раз по i, k раз по j)
for i in range(k):
    temp_row = [] # Временная строка
    for j in range(k):
        # 8. Копируем значение из [r+i][c+j]
        value = matrix[r + i][c + j]
        temp_row.append(value)
    # Квадрат [temp_square] будет, например, [[2, 3], [5, 6]]
    temp_square.append(temp_row)

# 9. Создаем пустой k x k квадрат для *повернутых* данных.
#    Мы заполняем его нулями, чтобы создать "каркас".
rotated_square = []
for i in range(k):
    rotated_square.append([0] * k) # [0] * k создает [0, 0] (для k=2)

# 10. Заполняем повернутый квадрат по "заклинанию"
for i in range(k):
    for j in range(k):
        # Эта формула поворачивает по часовой стрелке
        rotated_square[i][j] = temp_square[k - 1 - j][i]
# rotated_square теперь [[5, 2], [6, 3]]

# 11. "Вклеиваем" повернутые значения обратно в matrix
for i in range(k):
    for j in range(k):
        # Кладем значение в ту же "базовую" ячейку [r+i][c+j]
        matrix[r + i][c + j] = rotated_square[i][j]
# matrix теперь [[1, 5, 2], [4, 6, 3], [7, 8, 9]]

# 12. Проходим по каждой "строке" (row) в нашей matrix
for row in matrix:
    # 13. Превращаем числа [1, 5, 2] в текст ['1', '5', '2']
    str_row = map(str, row)

    # 14. Склеиваем ['1', '5', '2'] через пробел в '1 5 2'
    output_line = ' '.join(str_row)

    # 15. Печатаем готовую строку
    print(output_line)