# write code that adds or subtracts binary, decimal, and hexadecimal numbers.
# include a menu that allows the user to select the type of number they want to enter.
# include error trapping for any incorect input.
# include functions in each of the three number systems to convert to numbers.

class Number():
    def __init__(self, i_a, i_b):
        self.i_a = i_a
        self.i_b = i_b
        self.a = 0
        self.b = 0
        self.r = 0
        self.o = ""

    def add(self):
        return a + b

    def subt(self):
        return a - b

    def mult(self):
        return a * b

    def div(self):
        return a // b, a % b

class Binary(Number):
    def __init__(self, i_a, i_b):
        super().__init__(i_a, i_b)

    def bin_to_num(self):
        for i in range(len(str(self.i_a))):
            self.a += (2 ** i) * int(str(self.i_a)[::-1][i])

        for i in range(len(str(self.i_b))):
            self.b += (2 ** i) * int(str(self.i_b)[::-1][i])

    def num_to_bin(self):
        i = 0
        while True:
            if 2 ** i >= self.r:
                break
            i += 1

        for num in range(i - 1, -1, -1):
            if self.r >= 2 ** num:
                self.r -= 2 ** num
                self.o += "1"
            else:
                self.o += "0"

class Decimal(Number):
    def __init__(self, i_a, i_b):
        super().__init__(i_a, i_b)



def main():
    print("Welcome to the programmer calculator!")
    print("What would you like to calculate?")
    print("1. Binary")
    print("2. Decimal")
    print("3. Hexadecimal")
    selection = input()

    if selection == "1":
        print("What would you like to do?")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        selection = input()
        if selection == "1":