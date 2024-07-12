from number import Number


class Decimal(Number):

    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)

    def bin_to_dec(self, binary):
        output = 0
        binary = str(binary)[::-1]
        for i in range(len(binary)):
            output += int(binary[i]) * (2**i)

        return str(output)

    def dec_to_bin(self, decimal):
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
    print(d.bin_to_dec(10001111))
    print(d.dec_to_bin(143))