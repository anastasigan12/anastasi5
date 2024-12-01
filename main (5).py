def read_matrix_from_input():
    """Читання матриці з введення користувача"""
    matrix = [
        [3, 4, 3],
        [3, 4, 2, 2],
        [2, 1, 5, 1],
        [5, 2, 1, 4]
    ]
    return matrix

def find_min_of_max_elements(matrix):
    """Знаходимо мінімальний серед максимальних елементів стовпців"""
    if not matrix:
        return None
    
    # Трансформуємо матрицю для однакових кількостей елементів у стовпцях
    num_columns = max(len(row) for row in matrix)  # Найбільша кількість стовпців
    max_elements = []
    
    for col in range(num_columns):
        # Отримуємо максимальний елемент для кожного стовпця
        column_elements = [matrix[row][col] for row in range(len(matrix)) if col < len(matrix[row])]
        if column_elements:
            max_in_column = max(column_elements)
            max_elements.append(max_in_column)
    
    return min(max_elements)

def sort_matrix_by_rows(matrix):
    """Сортуємо матрицю по рядках за спадаючим порядком"""
    return [sorted(row, reverse=True) for row in matrix]

def print_matrix(matrix):
    """Виведення матриці на екран"""
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    matrix = read_matrix_from_input()

    if matrix:  # Перевіряємо, чи матриця не порожня
        min_of_max = find_min_of_max_elements(matrix)
        print(f"Мінімальний серед максимальних елементів стовпців: {min_of_max}")
        
        sorted_matrix = sort_matrix_by_rows(matrix)
        print("Відсортована матриця:")
        print_matrix(sorted_matrix)
    else:
        print("Матриця порожня.")

if __name__ == "__main__":
    main()