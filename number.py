class Number:
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator

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
        a = str(a)
        b = str(b)[::-1]
        output = 0
        for i in range(len(b)):
            if b[i] == "1":
                output = self.add(output, a + "0" * i)

        return output

    def div(self, a, b):
        pass

    def operation(self, a, b):
        if self.operator == "+":
            self.add(a, b)
        elif self.operator == "-":
            self.subt(a, b)
        elif self.operator == "*":
            self.mult(a, b)
        elif self.operator == "/":
            self.div(a, b)