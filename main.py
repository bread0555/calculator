class Number():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return a + b

    def subt(self):
        return a - b

    def mult(self):
        return a * b

    def div(self):
        return a // b, a % b

class Binary(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

class Decimal(Number):
    def __init__(self, a, b):
        super().__init__(a, b)

class Hexadecimal(Number):
    def __init__(self, a, b):
        super().__init__(a, b)