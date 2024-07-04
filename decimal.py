from main import Number


class Decimal(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.base = 10

    def div(self):
        self.result = round(int(self.a) / int(self.b), 2)

    def num_to_dec(self):
        if int(self.result) == float(self.result):
            self.result = int(self.result)
        else:
            self.result = float(self.result)