from matrix2d import Matrix2D
from vector2d import Vector2D

class Solver:
    def __init__(self):
        pass # Клас Solver не потребує ініціалізації з певними даними

    def solve_cramer(self, A: Matrix2D, B: Vector2D):
        """
        Розв'язує систему лінійних рівнянь Ax = B методом Крамера.
        A: Об'єкт Matrix2D (матриця коефіцієнтів)
        B: Об'єкт Vector2D (вектор правих частин)
        Повертає Vector2D з розв'язком [x, y] або None, якщо матриця вироджена.
        """
        det_A = A.determinant()

        if A.is_singular():
            print("Матриця вироджена (визначник = 0). Система не має єдиного розв'язку.")
            return None

        # Створюємо матрицю Ax
        # Замінюємо перший стовпець A на вектор B
        Ax_data = [
            [B.x, A.data[0][1]],
            [B.y, A.data[1][1]]
        ]
        Ax = Matrix2D(Ax_data)
        det_Ax = Ax.determinant()

        # Створюємо матрицю Ay
        # Замінюємо другий стовпець A на вектор B
        Ay_data = [
            [A.data[0][0], B.x],
            [A.data[1][0], B.y]
        ]
        Ay = Matrix2D(Ay_data)
        det_Ay = Ay.determinant()

        x = det_Ax / det_A
        y = det_Ay / det_A

        return Vector2D(x, y)