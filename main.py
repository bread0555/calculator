class Number:

    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator
        self.result = ""

    def align_binary(self, binary_a: str, binary_b: str) -> (str, str):
        if len(binary_a) < len(binary_b):
            binary_a = "0" * (len(binary_b) - len(binary_a)) + binary_a
        elif len(binary_b) < len(binary_a):
            binary_b = "0" * (len(binary_a) - len(binary_b)) + binary_b
        return binary_a, binary_b

    def ones_loc(self, binary: str) -> int:
        for i in range(len(binary)):
            if binary[i] == "1":
                return i
        return 0

    def add(self, addend_a: str, addend_b: str) -> str:
        addend_a, addend_b = self.align_binary(addend_a, addend_b)

        addend_a = addend_a[::-1]
        addend_b = addend_b[::-1]
        carry = 0
        total = ""  # cant use sum as var name, re. builtin function

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
        minuend, subtrahend = self.align_binary(minuend, subtrahend)

        subtrahend = subtrahend[::-1]
        complement = ""

        for i in range(len(subtrahend)):  # cant minus as int, possible trailing 0s
            if subtrahend[i] == "0":
                complement += "1"
            elif subtrahend[i] == "1":
                complement += "0"

        complement = self.add(complement[::-1], "1")
        difference = self.add(minuend, complement)[-len(subtrahend):]

        ones_loc = self.ones_loc(difference)

        return difference[ones_loc:]

    def mult(self, multiplicand: str, multiplier: str) -> str:
        multiplier = str(multiplier)[::-1]
        product = 0

        for i in range(len(multiplier)):
            if multiplier[i] == "1":
                product = self.add(str(product), multiplicand + "0" * i)

        return str(product)

    def div(self, dividend: str, divisor: str) -> str:
        if divisor == "0":
            return "0"
        elif divisor == "1":
            return dividend
        elif len(dividend) < len(divisor):
            return "0"
        elif dividend == divisor:
            return "1"

        quotient = ""
        length = len(dividend)

        for i in range(len(dividend) - len(divisor), -1, -1):
            div_temp = divisor
            divisible = True
            div_temp = div_temp + "0" * i
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

        ones_loc = self.ones_loc(quotient)

        return quotient[ones_loc:]


class Binary(Number):

    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)

    def operate(self):
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)


class Decimal(Number):

    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)

    def dec_to_bin(self, decimal: str) -> str:
        decimal = int(decimal)
        ceiling = 0
        for i in range(decimal):
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
        output = 0
        binary = str(binary)[::-1]
        for i in range(len(binary)):
            output += int(binary[i]) * (2**i)

        return str(output)

    def operate(self):
        self.a = dec_to_bin(self.a)
        self.b = dec_to_bin(self.b)
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)
        self.result = bin_to_dec(self.result)


class Hexadecimal(Number):

    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.hexbin = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111"
        }

    def hex_to_bin(self, hexadecimal: str) -> str:
        output = ""
        for i in hexadecimal:
            output += self.hexbin[i]

        ones_loc = self.ones_loc(output)

        return output[ones_loc:]

    def bin_to_hex(self, binary: str) -> str:
        binary = "0" * (4 - len(binary) % 4) + binary

        binary_ls = []
        while binary:
            binary_ls.append(binary[:4])
            binary = binary[4:]

        hexbin_keys = list(self.hexbin.keys())
        hexbin_values = list(self.hexbin.values())

        output = ""
        for i in binary_ls:
            output += hexbin_keys[hexbin_values.index(i)]

        return output

    def operate(self):
        self.a = hex_to_bin(self.a)
        self.b = hex_to_bin(self.b)
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)
        self.result = bin_to_hex(self.result)


def main(): # add error trapping before data sent off to classes to calculate
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

    print("Welcome to the programmer's calculator")

    a = input("\nEnter the first number\n- ").strip()
    b = input("\nEnter the second number\n- ").strip()
    operator = input("\nEnter the operator (+, -, *, /)\n- ").strip()

    test = Decimal(a, b, None)
    try:
        test.bin_to_dec(test.a)
        test.bin_to_dec(test.b)
        num_sys = 1
    except ValueError:
        try:
            test.dec_to_bin(test.a)
            test.dec_to_bin(test.b)
            num_sys = 2
        except ValueError:
            num_sys = 3

    print(f"\nTrying to do {num_systems[num_sys]} {operations[operator]}?")
    correct_num_sys = input("Y/N: ").strip()

    if correct_num_sys.upper() != "Y":
        print("\nEnter number corresponding to number system to calc in:")
        num_sys = int(input("1. Binary\n2. Decimal\n3. Hexadecimal\n- "))

    if num_sys == 1:
        calc = Binary(a, b, operator)

    elif num_sys == 2:
        calc = Decimal(a, b, operator)

    elif num_sys == 3:
        calc = Hexadecimal(a, b, operator)

    calc.operate()

    print(f"\nIn {num_systems[num_sys]}, {a} {operator} {b} is")
    print(calc.result)

if __name__ == "__main__":
    main()
