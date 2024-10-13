class Calculator:

    calculation_type = "Arithmetic Operations"

    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"The Calculation type is: {cls.calculation_type}")
        return a * b
