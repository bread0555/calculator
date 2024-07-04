from main import Number


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