class Binary():
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator

# shouldnt need any conversions since calculations are in binary

    def decimal(self, variable):
        output = 0
        variable = str(variable)[::-1]
        for i in range(len(variable)):
            output += int(variable[i]) * (2 ** i)

        return output

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