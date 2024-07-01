num_systems = {
    1: "binary",
    2: "decimal",
    3: "hexadecimal"
}

operations = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division"
}


class Number():
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator
        self.result = None
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
        return self.result

    def num_to_sys(self):
        pass


class Binary(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.base = 2

    def num_to_bin(self):
        self.result = bin(self.result)


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


class Hexadecimal(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.base = 16

    def num_to_hexa(self):
        self.result = hex(self.result)


def predict_ns(a, b):
    try:
        test = Binary(a, b, None)
        test.sys_to_num()
        return 1
    except ValueError:
        try:
            test = Decimal(a, b, None)
            test.sys_to_num()
            return 2
        except ValueError:
            return 3


def main():
    print("Welcome to the programmer calculator.")

    print("Enter the first number:")
    a = input().strip()

    print("Enter the second number:")
    b = input().strip()

    print("Enter the operator: (+, -, *, /)")
    operator = input().strip()

    num_system = predict_ns(a, b)
    print(f"Are you trying to do {num_systems[num_system]} {operations[operator]}?")
    predicted_ns = input("Y/N: ")

    if predicted_ns.upper() != "Y":
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
        myclass.sys_to_num()
        myclass.operation()
        myclass.num_to_dec()

    elif num_system == 3:
        myclass = Hexadecimal(a, b, operator)
        myclass.sys_to_num()
        myclass.operation()
        myclass.num_to_hexa()

    else:
        return

    print(f"\nIn {num_systems[num_system]}, {a} {operator} {b} is:\n{myclass.fetch_output()")


if __name__ == "__main__":
    main()