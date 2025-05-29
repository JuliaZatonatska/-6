import os

class Matrix2D:
    def __init__(self, data=None):
        """
        Ініціалізує матрицю 2x2.

        """
        if data:
            if not (isinstance(data, list) and len(data) == 2 and
                    all(isinstance(row, list) and len(row) == 2 and
                        all(isinstance(val, (int, float)) for val in row) for row in data)):
                raise ValueError("Матриця повинна бути списком списків з 2x2 числових значень.")
            self.data = [row[:] for row in data] # Копіюємо дані, щоб уникнути посилань
        else:
            self.data = [[0.0, 0.0], [0.0, 0.0]]

    def __str__(self):
        """Повертає строкове представлення матриці."""
        return f"[[{self.data[0][0]:.2f}, {self.data[0][1]:.2f}],\n [{self.data[1][0]:.2f}, {self.data[1][1]:.2f}]]"

    def __repr__(self):
        """Повертає офіційне представлення об'єкта."""
        return f"Matrix2D({self.data})"

    def input_from_keyboard(self):

        print("Введіть елементи матриці 2x2:")
        for i in range(2):
            while True:
                try:
                    row_str = input(f"Введіть елементи рядка {i+1} через пробіл (наприклад, '1.0 2.5'): ")
                    elements = list(map(float, row_str.split()))
                    if len(elements) == 2:
                        self.data[i] = elements
                        break
                    else:
                        print("Помилка: Введіть рівно два числа.")
                except ValueError:
                    print("Помилка: Введіть дійсні числа.")

    def input_from_file(self, filename):

        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл '{filename}' не знайдено.")

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().split() # Розділяємо весь вміст файлу за пробілами та новими рядками
            try:
                if len(content) < 4:
                    raise ValueError(f"Файл '{filename}' містить недостатньо даних (очікується 4 числа).")
                values = list(map(float, content[:4])) # Беремо перші 4 числа
                self.data[0][0] = values[0]
                self.data[0][1] = values[1]
                self.data[1][0] = values[2]
                self.data[1][1] = values[3]
            except ValueError:
                raise ValueError(f"Файл '{filename}' містить нечислові дані або некоректний формат.")

    def output_to_screen(self):
        """Виведення матриці на екран."""
        print("Матриця:")
        print(self)

    def output_to_file(self, filename):
        """Виведення матриці у файл."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(self) + "\n")
            print(f"Матриця успішно записана у файл '{filename}'.")
        except IOError as e:
            print(f"Помилка запису у файл '{filename}': {e}")

    def determinant(self):
        """Обчислює визначник матриці 2x2."""
        return (self.data[0][0] * self.data[1][1]) - (self.data[0][1] * self.data[1][0])

    def is_singular(self, tolerance=1e-9):
        """
        Перевіряє, чи є матриця виродженою (singular).

        """
        return abs(self.determinant()) < tolerance