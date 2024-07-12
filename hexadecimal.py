from number import Number


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

    def bin_to_hex(self, binary):
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

    def hex_to_bin(self, hexadecimal):
        output = ""
        for i in hexadecimal:
            output += self.hexbin[i]

        ones_loc = self.ones_loc(output)

        return output[ones_loc:]


def main():
    h = Hexadecimal(None, None, None)
    print(h.bin_to_hex("1101011101"))
    print(h.hex_to_bin("35D"))


if __name__ == "__main__":
    main()