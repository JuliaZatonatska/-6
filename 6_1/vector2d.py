class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        """Ініціалізує 2D-вектор."""
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Компоненти вектора повинні бути числами.")
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """Повертає строкове представлення вектора."""
        return f"[{self.x:.2f}, {self.y:.2f}]"

    def __repr__(self):
        """Повертає офіційне представлення об'єкта."""
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Можна додавати лише об'єкти Vector2D.")
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Можна віднімати лише об'єкти Vector2D.")
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Множити вектор можна лише на число (скаляр).")
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """Множення скаляра на вектор (для операції scalar * vector)."""
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        """Ділення вектора на скаляр."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Ділити вектор можна лише на число (скаляр).")
        if scalar == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return Vector2D(self.x / scalar, self.y / scalar)

    def dot_product(self, other):
        """Скалярний добуток двох векторів."""
        if not isinstance(other, Vector2D):
            raise TypeError("Скалярний добуток можна обчислювати лише з об'єктом Vector2D.")
        return (self.x * other.x) + (self.y * other.y)

    def magnitude(self):
        """Обчислює довжину (магнітуду) вектора."""
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        """Нормалізує вектор до одиничної довжини."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Неможливо нормалізувати нульовий вектор.")
        return self / mag