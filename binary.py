from main import Number


class Binary(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.base = 2 # not needed if not using int() builtin function

    def decimal(self, variable):
        output = 0
        variable = str(variable)[::-1]
        for i in range(len(variable)):
            output += int(variable[i]) * (2 ** i)

        return output

    def binary(self, variable):
        i = 0
        while True:
            if 2 ** i >= variable:
                break
            i += 1

        output = ""
        for i in range(i - 1, -1, -1):
            if variable >= 2 ** i:
                output += "1"
                variable -= 2 ** i
            else:
                output += "0"

        return output


    def add(self, a, b):
        a = str(a)
        b = str(b)

        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b

        a = a[::-1]
        b = b[::-1]

        spare = 0
        output = ""
        for i in range(len(a)):
            result = int(a[i]) + int(b[i]) + spare
            if result == 0:
                output += "0"
                spare = 0
            elif result == 1:
                output += "1"
                spare = 0
            elif result == 2:
                output += "0"
                spare = 1
            elif result == 3:
                output += "1"
                spare = 1

        if spare == 1:
            output += "1"

        return output[::-1]

    def subt(self, a, b):
        a = str(a)
        b = str(b)

        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b

        b = b[::-1]
        b_new = ""
        for i in range(len(b)):
            if b[i] == "0":
                b_new += "1"
            elif b[i] == "1":
                b_new += "0"

        b_new = b_new[::-1]
        b_new = self.add(b_new, "1")

        return self.add(a, b_new)[-len(b):]

    def mult(self, a, b):
        pass

    def div(self, a, b):
        pass