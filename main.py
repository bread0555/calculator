class Number:

    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator

    def align_binary(self, binary_a, binary_b):
        if len(binary_a) < len(binary_b):
            binary_a = "0" * (len(binary_b) - len(binary_a)) + binary_a
        elif len(b) < len(binary_a):
            binary_b = "0" * (len(binary_a) - len(binary_b)) + binary_b
        return binary_a, binary_b

    def ones_loc(self, binary):
        for i in range(len(binary)):
            if binary[i] == "1":
                return i
        return 0

    def add(self, addend_a, addend_b):
        addend_a = str(addend_a)
        addend_b = str(addend_b)

        addend_a, addend_b = self.align_binary(addend_a, addend_b)

        addend_a = addend_a[::-1]
        addend_b = addend_b[::-1]
        carry = 0
        total = ""  # cant use sum, re. builtin function

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

    def subt(self, minuend, subtrahend):
        minuend = str(minuend)
        subtrahend = str(subtrahend)

        if len(minuend) < len(subtrahend):
            minuend = "0" * (len(subtrahend) - len(minuend)) + minuend
        elif len(subtrahend) < len(minuend):
            subtrahend = "0" * (len(minuend) - len(subtrahend)) + subtrahend

        subtrahend = subtrahend[::-1]
        complement = ""

        for i in range(len(subtrahend)):  # cant minus, possible trailing 0s
            if subtrahend[i] == "0":
                complement += "1"
            elif subtrahend[i] == "1":
                complement += "0"

        complement = self.add(complement[::-1], "1")
        difference = self.add(minuend, complement)[-len(subtrahend):]

        return difference[self.ones_loc(difference):]

    def mult(self, multiplicand, multiplier):
        multiplicand = str(multiplicand)
        multiplier = str(multiplier)[::-1]
        product = 0

        for i in range(len(multiplier)):
            if multiplier[i] == "1":
                product = self.add(product, multiplicand + "0" * i)

        return str(product)

    def div(self, dividend, divisor):
        dividend = str(dividend)
        divisor = str(divisor)

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

        return quotient[self.ones_loc(quotient):]

    def operate(self, a, b):
        if self.operator == "+":
            self.add(a, b)
        elif self.operator == "-":
            self.subt(a, b)
        elif self.operator == "*":
            self.mult(a, b)
        elif self.operator == "/":
            self.div(a, b)


# def predict_ns(a, b):
#     try:
#         test = Binary(a, b, None)
#         test.sys_to_num()
#         return 1
#     except ValueError:
#         try:
#             test = Decimal(a, b, None)
#             test.sys_to_num()
#             return 2
#         except ValueError:
#             return 3

num_systems = {1: "binary", 2: "decimal", 3: "hexadecimal"}

operations = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division"
}


def main():
    print("Welcome to the programmer calculator.")

    print("Enter the first number:")
    a = input().strip()

    print("Enter the second number:")
    b = input().strip()

    print("Enter the operator: (+, -, *, /)")
    operator = input().strip()

    num_system = predict_ns(a, b)
    print(
        f"Are you trying to do {num_systems[num_system]} {operations[operator]}?"
    )
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

    print(
        f"\nIn {num_systems[num_system]}, {a} {operator} {b} is:\n{myclass.fetch_output()}"
    )



if __name__ == "__main__":
    main()