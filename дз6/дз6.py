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
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Трикутник (Сторони: {self.side1}, {self.side2}, {self.side3})"

class Trapezoid(Shape):
    def __init__(self, base1, base2, side1, side2):
        self.base1 = base1 # Одна основа
        self.base2 = base2 # Інша основа
        self.side1 = side1 # Одна бічна сторона
        self.side2 = side2 # Інша бічна сторона

    def area(self):


        raise NotImplementedError("Обчислення площі трапеції вимагає висоти або більш складних геометричних формул для визначення висоти з бічних сторін. Для спрощення, припустимо, що висота трапеції буде додатковим параметром.")

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def __str__(self):
        return f"Трапеція (Основи: {self.base1}, {self.base2}, Бічні сторони: {self.side1}, {self.side2})"

class Parallelogram(Shape):
    def __init__(self, side1, side2, height):
        self.side1 = side1 # Одна сторона
        self.side2 = side2 # Інша сторона (суміжна)
        self.height = height # Висота, проведена до side1 (або side2)

    def area(self):
        # Площа паралелограма = основа * висота.
        # Припустимо, що height - це висота, проведена до side1.
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

    def perimeter(self): # Для круга це довжина кола
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Круг (Радіус: {self.radius})"

    def process_file(filepath):

        shapes = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()  # Розділяємо рядок на частини за пробілами
                if not parts:  # Пропускаємо порожні рядки
                    continue

                shape_type = parts[0]
                params = [float(p) for p in parts[1:]]  # Перетворюємо параметри на числа

                shape = None
                if shape_type == "Triangle":
                    # Трикутник: side1, side2, side3
                    if len(params) == 3:
                        shape = Triangle(*params)
                    else:
                        print(f"Помилка: Неправильна кількість параметрів для Трикутника в {filepath}: {line.strip()}")
                elif shape_type == "Rectangle":
                    # Прямокутник: length, width
                    if len(params) == 2:
                        shape = Rectangle(*params)
                    else:
                        print(
                            f"Помилка: Неправильна кількість параметрів для Прямокутника в {filepath}: {line.strip()}")
                elif shape_type == "Trapezoid":

                    if len(params) == 5:  # base1, base2, side1, side2, height
                        shape = Trapezoid(*params[:4])
                        print(
                            f"Помилка: Трапеція вимагає 5 параметрів (основи, бічні сторони, висота) для обчислення площі у {filepath}: {line.strip()}")
                        print("Пропускаємо цю трапецію, оскільки висота не надана або неправильно.")
                        continue
                    else:
                        print(
                            f"Помилка: Неправильна кількість параметрів для Трапеції в {filepath}: {line.strip()}. Очікується 5 (включаючи висоту).")
                        continue  # Пропускаємо цю фігуру

                elif shape_type == "Parallelogram":
                    # Паралелограм: side1, side2, height
                    if len(params) == 3:
                        shape = Parallelogram(*params)
                    else:
                        print(
                            f"Помилка: Неправильна кількість параметрів для Паралелограма в {filepath}: {line.strip()}")
                elif shape_type == "Circle":
                    # Круг: radius
                    if len(params) == 1:
                        shape = Circle(*params)
                    else:
                        print(f"Помилка: Неправильна кількість параметрів для Круга в {filepath}: {line.strip()}")
                else:
                    print(f"Помилка: Невідомий тип фігури '{shape_type}' в {filepath}: {line.strip()}")

                if shape:
                    try:
                        # Перевіряємо, чи можна обчислити площу (наприклад, для трапеції без висоти)
                        shape.area()
                        shapes.append(shape)
                    except NotImplementedError as e:
                        print(f"Помилка обчислення для {shape_type} у {filepath}: {e}. Пропускаємо цю фігуру.")
                    except ValueError as e:  # Для трикутника, якщо сторони не утворюють дійсний трикутник
                        print(f"Помилка даних для {shape_type} у {filepath}: {e}. Пропускаємо цю фігуру.")

        return shapes


    class Trapezoid(Shape):
        def __init__(self, base1, base2, side1, side2, height):
            self.base1 = base1
            self.base2 = base2
            self.side1 = side1
            self.side2 = side2
            self.height = height  # Висота додана сюди для спрощення обчислення площі

        def area(self):
            return 0.5 * (self.base1 + self.base2) * self.height

        def perimeter(self):
            return self.base1 + self.base2 + self.side1 + self.side2

        def __str__(self):
            return f"Трапеція (Основи: {self.base1}, {self.base2}, Бічні сторони: {self.side1}, {self.side2}, Висота: {self.height})"

    def find_max_area_shape(all_shapes):
        """
        Знаходить фігуру з найбільшою площею серед усіх наданих фігур.
        """
        if not all_shapes:
            return None, None, None

        max_area = -1
        max_area_shape = None
        max_area_perimeter = None

        for shape in all_shapes:
            try:
                current_area = shape.area()
                if current_area > max_area:
                    max_area = current_area
                    max_area_shape = shape
                    max_area_perimeter = shape.perimeter()
            except NotImplementedError as e:
                print(f"Помилка обчислення площі для {type(shape).__name__}: {e}. Пропускаємо.")
            except ValueError as e:
                print(f"Помилка даних для {type(shape).__name__}: {e}. Пропускаємо.")

        return max_area_shape, max_area, max_area_perimeter