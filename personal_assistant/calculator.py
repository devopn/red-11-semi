class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a / b

    @staticmethod
    def calculate(expression):
        try:
            # Используем встроенную функцию eval с проверкой выражения
            return eval(expression)
        except ZeroDivisionError:
            raise ValueError("Ошибка: Деление на ноль.")
        except Exception:
            raise ValueError("Некорректное выражение.")
