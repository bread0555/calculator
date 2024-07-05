class Binary:
    def __init__(self, a, b, operator):
        pass
    
    def binary(self, variable, min_length: 0):
        i = 0
        while True:
            if 2 ** i >= variable:
                break
            i += 1

        output = ""
        for i in range(i - 1, -1, -1):
            if variable >= 2 ** i:
                output += "1"
                variable -= 2 ** i
            else:
                output += "0"

        if min_length > len(output):
            output = "0" * (min_length - len(output)) + output

        return output


class Hexadecimal():
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator

    def decimal(self, variable):
        output = 0
        variable = str(variable)[::-1].lower()
        for i in range(len(variable)):
            if "0" <= variable[i] <= "9":
                output += int(variable[i]) * (16 ** i)
            else:
                output += (ord(variable[i]) - ord("a") + 10) * (16 ** i)

        return output

    def binary(self, variable):
        output = ""
        for i in range(len(variable)):
            if "0" <= variable[i] <= "9":
                output += str(Binary.binary(int(variable[i]), 4))
            else:
                output += str(Binary.binary(ord(variable[i]) - ord("a") + 10, 4))

        return output

    def hexadecimal(self, variable):
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




# new goal:
# instead of converting to decimals to perform calculations
# convert to binary to perform calculations instead