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

        b_new = self.add(b_new[::-1], "1")
        output = self.add(a, b_new)[-len(b):]

        one_location = 0

        for i in range(len(output)):
            if output[i] == "1":
                one_location = i
                break

        return output[one_location:]

    def mult(self, a, b):
        a = str(a)
        b = str(b)[::-1]
        output = 0

        for i in range(len(b)):
            if b[i] == "1":
                output = self.add(output, a + "0" * i)

        return str(output)

    def div(self, a, b):
        a = str(a)
        b = str(b)

        if b == 0:
            return 0
        elif len(a) < len(b):
            return "0"
        elif a == b:
            return "1"

        a_new = a
        output = ""
        length = len(a)

        for i in range(len(a) - len(b), -1, -1):
            b_new = b
            divisable = True
            b_new = b_new + "0" * i
            if len(a_new) < length:
                a_new = "0" * (length - len(a_new)) + a_new
            elif len(a_new) > length:
                b_new = "0" * (len(a_new) - len(b_new)) + b_new
            for j in range(len(b_new)):
                if a_new[j] > b_new[j]:
                    break
                elif a_new[j] < b_new[j]:
                    divisable = False
                    break
            if divisable:
                output += "1"
                a_new = self.subt(a_new, b_new)
            else:
                output += "0"
            length -= 1

        return output


    def operate(self, a, b):
        if self.operator == "+":
            self.add(a, b)
        elif self.operator == "-":
            self.subt(a, b)
        elif self.operator == "*":
            self.mult(a, b)
        elif self.operator == "/":
            self.div(a, b)


number = Number(1101, 1011, "+")