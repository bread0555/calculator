from main import Number


class Hexadecimal(Number):
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        self.base = 16

    def decimal(self, variable):
        output = 0
        variable = str(variable)[::-1].lower()
        for i in range(len(variable)):
            if "0" <= variable[i] <= "9":
                output += int(variable[i]) * (16 ** i)
            else:
                output += (ord(variable[i]) - ord("a") + 10) * (16 ** i)

        return output

    def hexadecimal(variable):
        quotient = variable
        remainder = 0
        output = ""
        while quotient != 0:
            remainder = quotient % 16
            if 0 <= remainder <= 9:
                output += str(remainder)
            else:
                output += chr(remainder + ord("a") - 10)
            quotient = quotient // 16

        return output[::-1]


    def num_to_hexa(self):
        self.result = hex(int(self.result))