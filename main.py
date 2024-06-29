# write code that adds or subtracts binary, decimal, and hexadecimal numbers.
# include a menu that allows the user to select the type of number they want to enter.
# include error trapping for any incorect input.
# include functions in each of the three number systems to convert to numbers.

class Number():
    def __init__(self, input_a, input_b, input_operator):
        self.input_a = input_a
        self.input_b = input_b
        self.input_operator = input_operator
        self.a = 0
        self.b = 0
        self.result = 0
        self.output = 0
        self.base = 10

    def add(self):
        self.result = self.a + self.b

    def subt(self):
        self.result = self.a - self.b

    def mult(self):
        self.result = self.a * self.b

    def div(self):
        self.result = [self.a // self.b, self.a % self.b]

    def operator_selector(self):
        if self.input_operator == "+":
            self.add()
        elif self.input_operator == "-":
            self.subt()
        elif self.input_operator == "*":
            self.mult()
        elif self.input_operator == "/":
            self.div()

    def numsys_to_num(self):
        self.a = int(self.input_a, self.base)
        self.b = int(self.input_b, self.base)

    def fetch_output(self):
        return self.output


class Binary(Number):
    def __init__(self, input_a, input_b, i_operator):
        super().__init__(input_a, input_b, i_operator)
        self.base = 2

    def num_to_bin(self):
        self.output = bin(self.result)


class Decimal(Number):
    def __init__(self, i_a, i_b, i_o):
        super().__init__(i_a, i_b, i_o)


class Hexadecimal(Number):
    def __init__(self, i_a, i_b, i_o):
        super().__init__(i_a, i_b, i_o)
        self.base = 16

    def num_to_hexa(self):
        self.output = hex(self.result)


def main():
    print("Welcome to the programmer calculator!")
    print("Enter the first number:")
    a = input()
    print("Enter the second number:")
    b = input()
    print("Enter the operator: (+, -, *, /)")
    operator = input()
    print("Enter the number system you want to use:")
    print("1. Binary\n2. Decimal\n3. Hexadecimal")
    num_system = input()
    if num_system == "1":
        myclass = Binary(a, b, operator)
        myclass.numsys_to_num()
        myclass.operator_selector()
        myclass.num_to_bin()
    elif num_system == "2":
        myclass = Decimal(a, b, operator)
        myclass.operator_selector()
    elif num_system == "3":
        myclass = Hexadecimal(a, b, operator)
        myclass.numsys_to_num()
        myclass.operator_selector()
        myclass.num_to_hexa()
    print(myclass.fetch_output())