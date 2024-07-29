class Number:

    def __init__(self, a, b, operator):
        self.bin_dig = ["0", "1"]
        if self.check_binary(a):
            self.a = a
        else:
            self.a = "0"
        if self.check_binary(b):
            self.b = b
        else:
            self.b = "0"
        if self.check_operator(operator):
            self.operator = operator
        else:
            self.operator = "+"
        self.result = ""

    def check_binary(self, a, b="0") -> bool:
        if isinstance(a, int):
            a = str(a)

        if isinstance(b, int):
            b = str(b)

        if not isinstance(a, str) or not isinstance(b, str):
            return False

        ab = f"{a}{b}"
        return all(i in self.bin_dig for i in ab)

    def check_operator(self, operator) -> bool:
        operators = ["+", "-", "*", "/"]
        if not isinstance(operator, str):
            return False

        if operator not in operators:
            return False

        return True

    def add(self, addend_a: str, addend_b: str) -> str:
        if not self.check_binary(addend_a, addend_b):
            return "0"

        if len(addend_a) < len(addend_b):
            addend_a = "0" * (len(addend_b) - len(addend_a)) + addend_a
        elif len(addend_b) < len(addend_a):
            addend_b = "0" * (len(addend_a) - len(addend_b)) + addend_b

        addend_a = addend_a[::-1]
        addend_b = addend_b[::-1]
        carry = 0
        total = ""

        for i in range(len(addend_a)):
            result = int(addend_a[i]) + int(addend_b[i]) + carry
            if result == 0:
                total += "0"
                carry = 0
            elif result == 1:
                total += "1"
                carry = 0
            elif result == 2:
                total += "0"
                carry = 1
            elif result == 3:
                total += "1"
                carry = 1

        if carry == 1:
            total += "1"

        return total[::-1]

    def subt(self, minuend: str, subtrahend: str) -> str:
        if not self.check_binary(minuend, subtrahend):
            return "0"

        if len(minuend) < len(subtrahend):
            minuend = "0" * (len(subtrahend) - len(minuend)) + minuend
        elif len(subtrahend) < len(minuend):
            subtrahend = "0" * (len(minuend) - len(subtrahend)) + subtrahend

        subtrahend = subtrahend[::-1]
        complement = ""

        for i in range(len(subtrahend)):
            if subtrahend[i] == "0":
                complement += "1"
            elif subtrahend[i] == "1":
                complement += "0"

        complement = self.add(complement[::-1], "1")
        difference = self.add(minuend, complement)[-len(subtrahend):]

        ones_loc = 0
        for i in range(len(difference)):
            if difference[i] == "1":
                ones_loc = i
                break

        return difference[ones_loc:]

    def mult(self, multiplicand: str, multiplier: str) -> str:
        if not self.check_binary(multiplicand, multiplier):
            return "0"

        multiplier = str(multiplier)[::-1]
        product = "0"

        for i in range(len(multiplier)):
            if multiplier[i] == "1":
                product = self.add(str(product), multiplicand + "0" * i)

        return str(product)

    def div(self, dividend: str, divisor: str) -> str:
        if not self.check_binary(dividend, divisor):
            return "0"

        if divisor == "1":
            return dividend
        elif divisor == dividend:
            return "1"
        elif divisor == "0" or len(dividend) < len(divisor):
            return "0"

        quotient = ""
        length = len(dividend)

        for i in range(len(dividend) - len(divisor), -1, -1):
            div_temp = divisor + "0" * i
            divisible = True
            if len(dividend) < length:
                dividend = "0" * (length - len(dividend)) + dividend
            elif len(dividend) > length:
                div_temp = "0" * (len(dividend) - len(div_temp)) + div_temp
            for j in range(len(div_temp)):
                if dividend[j] > div_temp[j]:
                    break
                elif dividend[j] < div_temp[j]:
                    divisible = False
                    break

            if divisible:
                quotient += "1"
                dividend = self.subt(dividend, div_temp)
            else:
                quotient += "0"
            length -= 1

        ones_loc = 0
        for i in range(len(quotient)):
            if quotient[i] == "1":
                ones_loc = i
                break

        return quotient[ones_loc:]

    def operate(self):
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)


class Binary(Number):

    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)


class Decimal(Number):

    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.dec_dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if self.check_decimal(a):
            self.a = a
        else:
            self.a = "0"
        if self.check_decimal(b):
            self.b = b
        else:
            self.b = "0"

    def check_decimal(self, a, b="0") -> bool:
        if isinstance(a, int):
            a = str(a)

        if isinstance(b, int):
            b = str(b)

        if not isinstance(a, str) or not isinstance(b, str):
            return False

        ab = f"{a}{b}"
        return all(i in self.dec_dig for i in ab)

    def dec_to_bin(self, decimal: str) -> str:
        if not self.check_decimal(decimal):
            return "0"

        decimal = int(decimal)
        ceiling = 0
        for i in range(int(decimal)):
            if 2**i >= decimal:
                ceiling = i
                break

        output = ""
        for i in range(ceiling - 1, -1, -1):
            if decimal >= 2**i:
                output += "1"
                decimal -= 2**i
            else:
                output += "0"

        return output

    def bin_to_dec(self, binary: str) -> str:
        if not self.check_binary(binary):
            return "0"

        output = 0
        binary = str(binary)[::-1]
        for i in range(len(binary)):
            output += int(binary[i]) * (2**i)

        return str(output)

    def operate(self):
        self.a = self.dec_to_bin(self.a)
        self.b = self.dec_to_bin(self.b)
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)
        self.result = self.bin_to_dec(self.result)


class Hexadecimal(Number):

    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.hex_dig = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C",
            "D", "E", "F"
        ]
        if self.check_hexadecimal(a):
            self.a = a
        else:
            self.a = "0"
        if self.check_hexadecimal(b):
            self.b = b
        else:
            self.b = "0"

        self.hex_binaries = [
            "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111",
            "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"
        ]

    def check_hexadecimal(self, a, b="0") -> bool:
        if not isinstance(a, str) or not isinstance(b, str):
            return False

        ab = f"{a}{b}"
        return all(i in self.hex_dig for i in ab)

    def hex_to_bin(self, hexadecimal: str) -> str:
        if not self.check_hexadecimal(hexadecimal):
            return "0"

        output = ""
        for i in range(len(hexadecimal)):
            for j in range(len(self.hex_dig)):
                if hexadecimal[i] == self.hex_dig[j]:
                    output += self.hex_binaries[j]

        ones_loc = 0
        for i in range(len(output)):
            if output[i] == "1":
                ones_loc = i
                break

        return output[ones_loc:]

    def bin_to_hex(self, binary: str) -> str:
        if not self.check_binary(binary):
            return "0"

        binary = "0" * (4 - len(binary) % 4) + binary

        binary_ls = []
        while binary:
            binary_ls.append(binary[:4])
            binary = binary[4:]

        output = ""
        for i in binary_ls:
            output += self.hex_dig[self.hex_binaries.index(i)]

        return output

    def operate(self):
        self.a = self.hex_to_bin(self.a)
        self.b = self.hex_to_bin(self.b)
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)
        self.result = self.bin_to_hex(self.result)


def main():
    num_systems = {1: "binary", 2: "decimal", 3: "hexadecimal"}

    operations = {
        "+": "addition",
        "-": "subtraction",
        "*": "multiplication",
        "/": "division"
    }

    print("Welcome to the programmer's calculator")

    print("\nInstructons:")
    print("1. Enter two numbers from the same number system.")
    print("2. Enter an operator (+, -, *, /).")
    print("3. Select the number system that your two numbers are in.")
    print("4. The result will be displayed in the number system you selected.")
    input("\nPress enter to continue ")

    a = input("\nEnter the first number\n- ").strip().upper()
    b = input("\nEnter the second number\n- ").strip().upper()
    operator = input("\nEnter the operator (+, -, *, /)\n- ").strip()

    if operator not in operations:
        print("\nInvalid input: Operator must be +, -, *, or /")
        return

    test = Binary(None, None, None)
    test_bin = test.check_binary(f"{a}{b}")
    del test

    test = Decimal(None, None, None)
    test_dec = test.check_decimal(f"{a}{b}")
    del test

    test = Hexadecimal(None, None, None)
    test_hex = test.check_hexadecimal(f"{a}{b}")
    del test

    if test_bin:
        num_sys = 1
    elif test_dec:
        num_sys = 2
    elif test_hex:
        num_sys = 3
    else:
        print("\nInvalid input: A, B must be of valid number system")
        return

    print(f"\nTrying to do {num_systems[num_sys]} {operations[operator]}?")
    correct_num_sys = input("Y/N: ").strip()

    if correct_num_sys.upper() != "Y" and correct_num_sys:
        print("\nEnter number corresponding to number system to calculate in:")
        num_sys = int(input("1. Binary\n2. Decimal\n3. Hexadecimal\n- "))

        if num_sys not in num_systems:
            print("\nInvalid input: Number system must be 1, 2, or 3")
            return

    if num_sys == 1 and test_bin:
        calc = Binary(a, b, operator)

    elif num_sys == 2 and test_dec:
        calc = Decimal(a, b, operator)

    elif num_sys == 3 and test_hex:
        calc = Hexadecimal(a, b, operator)

    else:
        print("\nInvalid input: A, B must be valid for selected number system")
        return

    calc.operate()

    print(f"\nIn {num_systems[num_sys]}, {a} {operator} {b} = {calc.result}")


if __name__ == "__main__":
    main()
