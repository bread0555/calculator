class Number():
    def __init__(self, a, b, operator):
        self.operator = operator
        self.a = a
        self.b = b
        self.result = 0
        self.output = ""
        self.base = 10

    def add(self):
        self.result = int(self.a) + int(self.b)

    def subt(self):
        self.result = int(self.a) - int(self.b)

    def mult(self):
        self.result = int(self.a) * int(self.b)

    def div(self):
        self.result = int(self.a) // int(self.b)

    def operation(self):
        print(self.a)
        print(self.b)
        if self.operator == "+":
            self.add()
        elif self.operator == "-":
            self.subt()
        elif self.operator == "*":
            self.mult()
        elif self.operator == "/":
            self.div()

    def sys_to_num(self):
        self.a = int(str(self.a), self.base)
        self.b = int(str(self.b), self.base)

    def fetch_output(self):
        return self.output


class Binary(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.base = 2

    def num_to_bin(self):
        self.output = bin(self.result)


class Decimal(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)

    def num_to_dec(self):
        self.output = int(self.result)


class Hexadecimal(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.base = 16

    def num_to_hexa(self):
        self.output = hex(self.result)


def main():
    print("Welcome to the programmer calculator.")

    print("Enter the first number:")
    a = input()

    print("Enter the second number:")
    b = input()

    print("Enter the operator: (+, -, *, /)")
    operator = input()

    print("Enter the number system you want to use:")
    print("1. Binary\n2. Decimal\n3. Hexadecimal")
    num_system = int(input())

    if num_system == 1:
        myclass = Binary(a, b, operator)
        myclass.sys_to_num()
        myclass.operation()
        myclass.num_to_bin()

    elif num_system == 2:
        myclass = Decimal(a, b, operator)
        myclass.operation()
        myclass.num_to_dec()

    elif num_system == 3:
        myclass = Hexadecimal(a, b, operator)
        myclass.sys_to_num()
        myclass.operation()
        myclass.num_to_hexa()

    print(myclass.fetch_output())


if __name__ == "__main__":
    main()