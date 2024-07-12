from number import Number


class Decimal(Number):

    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)

    def decimal(self, binary):
        output = 0
        binary = str(binary)[::-1]
        for i in range(len(binary)):
            output += int(binary[i]) * (2**i)

        return str(output)

    def binary(self, decimal):
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


if __name__ == "__main__":  # testing
    d = Decimal("1", "2", "+")
    print(d.decimal(10001111))
    print(d.binary(143))