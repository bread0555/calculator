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

    def sys_to_num(self, variable):
        self.a = int(str(self.a), self.base)
        self.b = int(str(self.b), self.base)

    def fetch_output(self):
        return self.result

    def num_to_sys(self):
        pass


def sys_to_num(self, variable):
    output = 0
    variable = str(variable)
    for i in range(len(variable)):
        if "0" <= variable[i] <= "9":
            output += int(variable[i])
        else:
            output += (ord(variable[i]) - ord("a"))

class Binary(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.base = 2

    def sys_to_num(self, variable):
        output = 0
        variable = str(variable)[::-1]
        for i in range(len(variable)):
            output += int(variable[i]) * (2 ** i)
        return output

    def add(self, a, b):
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

        return(output[::-1])

    def num_to_bin(self):
        self.result = bin(int(self.result))


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

    def sys_to_num(self, variable):
        output = 0
        variable = str(variable)
        for i in range(len(variable)):
            if "0" <= variable[i] <= "9":
                output += int(variable[i])
            else:
                output += (ord(variable[i]) - ord("a"))

    
    def num_to_hexa(self):
        self.result = hex(int(self.result))


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

    print(f"\nIn {num_systems[num_system]}, {a} {operator} {b} is:\n{myclass.fetch_output()}")


if __name__ == "__main__":
    main()