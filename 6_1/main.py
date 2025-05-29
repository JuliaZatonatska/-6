import os
from matrix2d import Matrix2D
from vector2d import Vector2D
from solver import Solver

def read_data_from_files(matrix_filepath, rhs_filepath):
    systems = []

    if not os.path.exists(matrix_filepath):
        print(f"Помилка: Файл коефіцієнтів '{matrix_filepath}' не знайдено.")
        return []
    if not os.path.exists(rhs_filepath):
        print(f"Помилка: Файл правих частин '{rhs_filepath}' не знайдено.")
        return []

    try:
        with open(matrix_filepath, 'r', encoding='utf-8') as f_mat:
            matrix_lines = f_mat.readlines()

        with open(rhs_filepath, 'r', encoding='utf-8') as f_rhs:
            rhs_lines = f_rhs.readlines()

        if len(matrix_lines) != len(rhs_lines):
            print("Помилка: Кількість рядків у файлах коефіцієнтів та правих частин не збігається.")
            return []

        for i, (mat_line, rhs_line) in enumerate(zip(matrix_lines, rhs_lines)):
            try:
                # Читаємо коефіцієнти матриці
                mat_vals = list(map(float, mat_line.strip().split()))
                if len(mat_vals) != 4:
                    print(f"Помилка в файлі '{matrix_filepath}', рядок {i+1}: Очікується 4 коефіцієнти для матриці. Пропускаємо.")
                    continue
                matrix_data = [[mat_vals[0], mat_vals[1]], [mat_vals[2], mat_vals[3]]]
                matrix_A = Matrix2D(matrix_data)

                # Читаємо значення правої частини вектора
                rhs_vals = list(map(float, rhs_line.strip().split()))
                if len(rhs_vals) != 2:
                    print(f"Помилка в файлі '{rhs_filepath}', рядок {i+1}: Очікується 2 значення для вектора правої частини. Пропускаємо.")
                    continue
                vector_B = Vector2D(rhs_vals[0], rhs_vals[1])

                systems.append((matrix_A, vector_B))

            except ValueError:
                print(f"Помилка перетворення даних на число в рядку {i+1}. Пропускаємо.")
            except Exception as e:
                print(f"Невідома помилка при читанні даних з рядка {i+1}: {e}. Пропускаємо.")

    except IOError as e:
        print(f"Помилка читання файлів: {e}")
        return []
    return systems

if __name__ == "__main__":
    matrix_coefficients_file = "matrix_coefficients.txt"
    rhs_values_file = "rhs_values.txt"
    output_results_file = "solution_results.txt"

    solver = Solver()
    all_systems = read_data_from_files(matrix_coefficients_file, rhs_values_file)

    print("\n--- Розв'язання систем лінійних рівнянь ---")
    results = []
    if not all_systems:
        print("Немає систем для розв'язання.")
    else:
        for i, (matrix_A, vector_B) in enumerate(all_systems):
            print(f"\nСистема {i+1}:")
            print("Матриця A:")
            matrix_A.output_to_screen()
            print("Вектор B:", vector_B)

            solution = solver.solve_cramer(matrix_A, vector_B)

            if solution:
                print("Розв'язок [x, y]:", solution)
                results.append(f"Система {i+1}:\n  Матриця A: {matrix_A}\n  Вектор B: {vector_B}\n  Розв'язок: {solution}\n")
            else:
                print("Система не має єдиного розв'язку (матриця вироджена).")
                results.append(f"Система {i+1}:\n  Матриця A: {matrix_A}\n  Вектор B: {vector_B}\n  Розв'язок: Не має єдиного розв'язку (матриця вироджена).\n")

    try:
        with open(output_results_file, 'w', encoding='utf-8') as f_out:
            f_out.write("--- Результати розв'язання систем ЛАР ---\n\n")
            for res_str in results:
                f_out.write(res_str)
        print(f"\nРезультати записано у файл: '{output_results_file}'")
    except IOError as e:
        print(f"Помилка запису результатів у файл: {e}")