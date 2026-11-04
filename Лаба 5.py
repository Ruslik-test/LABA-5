import random

def create_matrix(n):
    """Функция формирования квадратной матрицы случайными числами"""
    matrix = []
    for i in range(n):
        row = [random.randint(-50, 50) for _ in range(n)]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """Функция вывода матрицы на экран"""
    for row in matrix:
        for elem in row:
            print(f"{elem:5}", end=" ")
        print()

def find_extreme_columns(matrix):
    """Поиск индексов столбцов с максимальным и минимальным элементами"""
    n = len(matrix)
    min_val = float('inf')
    max_val = float('-inf')
    min_col = 0
    max_col = 0
    
    # Проходим по столбцам
    for j in range(n):
        # Проходим по строкам
        for i in range(n):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_col = j
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_col = j
                
    return min_col, max_col

def swap_columns(matrix, col1, col2):
    """Функция обмена двух столбцов местами"""
    n = len(matrix)
    for i in range(n):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

def calc_main_diagonal_sum(matrix):
    """Вычисление суммы элементов главной диагонали"""
    n = len(matrix)
    diag_sum = 0
    for i in range(n):
        diag_sum += matrix[i][i]
    return diag_sum

def main():
    # 1. Ввод данных
    try:
        n = int(input("Введите размер квадратной матрицы (N): "))
        if n <= 0:
            print("Размер матрицы должен быть больше 0.")
            return
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")
        return

    # 2. Формирование и вывод исходной матрицы
    matrix = create_matrix(n)
    print("\n--- ИСХОДНАЯ МАТРИЦА ---")
    print_matrix(matrix)

    # 3. Поиск столбцов с экстремумами
    min_col, max_col = find_extreme_columns(matrix)
    print(f"\nСтолбец с мин. элементом (индекс): {min_col}")
    print(f"Столбец с макс. элементом (индекс): {max_col}")

    # 4. Обмен столбцов
    if min_col != max_col:
        swap_columns(matrix, min_col, max_col)
    else:
        print("Минимальный и максимальный элементы находятся в одном столбце. Обмен не требуется.")

    # 5. Вывод результирующей матрицы
    print("\n--- МАТРИЦА ПОСЛЕ ОБМЕНА СТОЛБЦОВ ---")
    print_matrix(matrix)

    # 6. Вычисление суммы главной диагонали
    diag_sum = calc_main_diagonal_sum(matrix)
    print(f"\nСумма элементов главной диагонали: {diag_sum}")

if __name__ == "__main__":
    main()