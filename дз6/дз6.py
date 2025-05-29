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