import math

class Shape:
    def area(self):
        raise NotImplementedError("Метод 'area' має бути реалізований у дочірньому класі.")

    def perimeter(self):
        """Обчислює периметр фігури. Має бути реалізовано в дочірніх класах."""
        raise NotImplementedError("Метод 'perimeter' має бути реалізований у дочірньому класі.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Прямокутник (Довжина: {self.length}, Ширина: {self.width})"

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Використовуємо формулу Герона для площі трикутника
        s = (self.side1 + self.side2 + self.side3) / 2
        # Перевірка на недійсний трикутник (може призвести до від'ємного числа під коренем)
        if s <= self.side1 or s <= self.side2 or s <= self.side3:
            raise ValueError("Недійсні сторони трикутника. Неможливо обчислити площу.")
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Трикутник (Сторони: {self.side1}, {self.side2}, {self.side3})"

# ОДИН ЄДИНИЙ і ПРАВИЛЬНИЙ клас Trapezoid
class Trapezoid(Shape):
    def __init__(self, base1, base2, side1, side2, height): # Тепер очікує 5 параметрів
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def __str__(self):
        return f"Трапеція (Основи: {self.base1}, {self.base2}, Бічні сторони: {self.side1}, {self.side2}, Висота: {self.height})"

class Parallelogram(Shape):
    def __init__(self, side1, side2, height):
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def area(self):
        return self.side1 * self.height

    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def __str__(self):
        return f"Паралелограм (Сторони: {self.side1}, {self.side2}, Висота: {self.height})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Круг (Радіус: {self.radius})"

def process_file(filepath):
    """
    Обробляє один файл, створює об'єкти фігур,
    обчислює площу та периметр, і повертає список всіх фігур.
    """
    shapes = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue

            shape_type = parts[0]
            params = [float(p) for p in parts[1:]]

            shape = None
            if shape_type == "Triangle":
                if len(params) == 3:
                    shape = Triangle(*params)
                else:
                    print(f"Помилка: Неправильна кількість параметрів для Трикутника в {filepath}: {line.strip()}. Очікується 3.")
            elif shape_type == "Rectangle":
                if len(params) == 2:
                    shape = Rectangle(*params)
                else:
                    print(f"Помилка: Неправильна кількість параметрів для Прямокутника в {filepath}: {line.strip()}. Очікується 2.")
            elif shape_type == "Trapezoid":
                # Тепер Trapezoid очікує 5 параметрів: base1, base2, side1, side2, height
                if len(params) == 5:
                    shape = Trapezoid(*params) # Передаємо всі 5 параметрів
                else:
                    print(f"Помилка: Неправильна кількість параметрів для Трапеції в {filepath}: {line.strip()}. Очікується 5 (основи, бічні сторони, висота).")
                    continue
            elif shape_type == "Parallelogram":
                if len(params) == 3:
                    shape = Parallelogram(*params)
                else:
                    print(f"Помилка: Неправильна кількість параметрів для Паралелограма в {filepath}: {line.strip()}. Очікується 3.")
            elif shape_type == "Circle":
                if len(params) == 1:
                    shape = Circle(*params)
                else:
                    print(f"Помилка: Неправильна кількість параметрів для Круга в {filepath}: {line.strip()}. Очікується 1.")
            else:
                print(f"Помилка: Невідомий тип фігури '{shape_type}' в {filepath}: {line.strip()}")

            if shape:
                try:
                    # Перевіряємо, чи можна обчислити площу (наприклад, для трикутника з недійсними сторонами)
                    shape.area() # Виклик area() для перевірки
                    shapes.append(shape)
                except ValueError as e: # Для трикутника, якщо сторони не утворюють дійсний трикутник
                    print(f"Помилка даних для {type(shape).__name__} у {filepath}: {e}. Пропускаємо цю фігуру.")
                except NotImplementedError as e:
                    # Цей випадок вже не повинен відбуватися, якщо класи правильно реалізовані
                    print(f"Непередбачена помилка обчислення для {type(shape).__name__} у {filepath}: {e}. Пропускаємо.")


    return shapes

def find_max_area_shape(all_shapes):
    """
    Знаходить фігуру з найбільшою площею серед усіх наданих фігур.
    """
    if not all_shapes:
        return None, None, None

    max_area = -1.0 # Початкове значення для максимальної площі
    max_area_shape = None
    max_area_perimeter = None

    for shape in all_shapes:
        try:
            current_area = shape.area()
            # Перевіряємо, чи площа дійсна (не NaN або нескінченність, що може бути від math.sqrt з від'ємним)
            if not math.isnan(current_area) and current_area > max_area:
                max_area = current_area
                max_area_shape = shape
                max_area_perimeter = shape.perimeter()
        except NotImplementedError as e:
            print(f"Помилка обчислення площі для {type(shape).__name__}: {e}. Пропускаємо.")
        except ValueError as e:
            print(f"Помилка даних для {type(shape).__name__}: {e}. Пропускаємо.")

    return max_area_shape, max_area, max_area_perimeter

if __name__ == "__main__":
    file_paths = ["input01.txt", "input02.txt", "input03.txt"]
    all_processed_shapes = []

    # Обробляємо кожен файл
    for fp in file_paths:
        print(f"\nОбробка файлу: {fp}")
        shapes_from_file = process_file(fp)
        all_processed_shapes.extend(shapes_from_file)

    # Знаходимо фігуру з найбільшою площею
    largest_shape, largest_area, largest_perimeter = find_max_area_shape(all_processed_shapes)

    print("\n--- Результат ---")
    if largest_shape:
        print(f"Фігура з найбільшою площею: {largest_shape}")
        print(f"Найбільша площа: {largest_area:.2f}")
        print(f"Периметр цієї фігури: {largest_perimeter:.2f}")
    else:
        print("Не знайдено жодної дійсної фігури для обробки.")