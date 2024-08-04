#  defining Number
class Number:

    #  initiate Number
    def __init__(self, a, b, operator):
        """
        Initiates Number class.

        Args:
            a: The first number.
            b: The second number.
            operator: The operator.

        Returns:

        """
        #  create variable with all characters of number system
        self.bin_dig = ["0", "1"]

        #  check if a is valid, if not, set a = "0"
        if self.check_binary(a):
            self.a = a
        else:
            self.a = "0"

        #  check if b is valid, if not, set b = "0"
        if self.check_binary(b):
            self.b = b
        else:
            self.b = "0"

        #  check if operator is valid, if not, set operator = "+"
        if self.check_operator(operator):
            self.operator = operator
        else:
            self.operator = "+"

        #  create empty variable to store the result of calculations
        self.result = ""

    #  define check_binary function
    def check_binary(self, a, b="0") -> bool:
        """
        Checks if arguments are valid binaries and returns a bool.

        Args:
            a: The first number.
            b: The second number (default value: "0").

        Returns:
            bool: The validity of a and b.
        """
        #  convert a into a string if it is of type int
        if isinstance(a, int):
            a = str(a)

        #  convert b into a string if it is of type int
        if isinstance(b, int):
            b = str(b)

        #  return False if a or b are not of type str
        if not isinstance(a, str) or not isinstance(b, str):
            return False

        #  concatinate a and b together
        ab = f"{a}{b}"
        #  return true if all values in ab are in bin_dig, else false
        return all(i in self.bin_dig for i in ab)

    #  define check_operator function
    def check_operator(self, operator) -> bool:
        """
        Checks if arguments are valid operators and returns a bool.

        Args:
            operator: The operator.

        Returns:
            bool: The validity of operator.
        """
        #  create variable defining all valid operators
        operators = ["+", "-", "*", "/"]
        #  return False if operator is not of type str
        if not isinstance(operator, str):
            return False

        #  return False if operator is not in operators
        if operator not in operators:
            return False

        #  else, return True
        return True

    #  define add function
    def add(self, addend_a: str, addend_b: str) -> str:
        """
        Adds two binary numbers and returns the total.

        Args:
            addend_a (str): The first number.
            addend_b (str): The second number.

        Returns:
            str: The total of addend_a and addend_b.
        """
        #  return "0" if addend_a or addend_b are not valid binaries
        if not self.check_binary(addend_a, addend_b):
            return "0"

        #  add trailing 0s to addend_a if shorter than addend_b
        if len(addend_a) < len(addend_b):
            addend_a = "0" * (len(addend_b) - len(addend_a)) + addend_a
        #  add trailing 0s to addend_b if shorter than addend_a
        elif len(addend_b) < len(addend_a):
            addend_b = "0" * (len(addend_a) - len(addend_b)) + addend_b

        #  reverse addend_a and addend_b
        addend_a = addend_a[::-1]
        addend_b = addend_b[::-1]
        #  create empty variable to store the carry of each iteration's sum
        carry = 0
        #  create empty variable to store total sum
        total = ""

        #  iterate through each character of addend_a
        for i in range(len(addend_a)):
            #  add the corresponding character of addend_a, addend_b, and carry
            result = int(addend_a[i]) + int(addend_b[i]) + carry
            #  if result is greater than 1, set carry to 1
            #  if result is less than 2, set carry to 0
            #  if result is odd, append "1" to total
            #  if result is even, append "0" to total
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

        #  if carry is 1, append "1" to total
        if carry == 1:
            total += "1"

        #  reverse total and return
        return total[::-1]

    #  define subtract function
    def subt(self, minuend: str, subtrahend: str) -> str:
        """
        Subtracts one binary number from another and returns the difference.

        Args:
            minuend (str): The first number.
            subtrahend (str): The second number.

        Returns:
            str: The difference of minuend and subtrahend.
        """
        #  return "0" if minuend or subtrahend are not valid binaries
        if not self.check_binary(minuend, subtrahend):
            return "0"

        #  add trailing zeros to minuend if shorter than subtrahend
        if len(minuend) < len(subtrahend):
            minuend = "0" * (len(subtrahend) - len(minuend)) + minuend
        #  add trailing zeros to subtrahend if shorter than minuend
        elif len(subtrahend) < len(minuend):
            subtrahend = "0" * (len(minuend) - len(subtrahend)) + subtrahend

        #  reverse subtrahend
        subtrahend = subtrahend[::-1]
        #  create empty variable to store the complement of subtrahend
        complement = ""

        #  iterate through each character of subtrahend
        for i in range(len(subtrahend)):
            #  if character is "0", append "1" to complement
            if subtrahend[i] == "0":
                complement += "1"
            #  if character is "1", append "0" to complement
            elif subtrahend[i] == "1":
                complement += "0"

        #  add 1 to the complement
        complement = self.add(complement[::-1], "1")
        #  calculate the difference by adding the minuend and the complement
        #  remove any characters after the length of the subtrahend
        difference = self.add(minuend, complement)[-len(subtrahend):]

        #  create a variable to store the index of the first "1"
        ones_loc = 0
        #  iterate through each character of difference
        for i in range(len(difference)):
            #  if character is "1", set ones_loc to the index and break
            if difference[i] == "1":
                ones_loc = i
                break

        #  return the difference with trailing zeros removed
        return difference[ones_loc:]

    #  define multiply function
    def mult(self, multiplicand: str, multiplier: str) -> str:
        """
        Multiplies two binary numbers and returns the product.

        Args:
            multiplicand (str): The first number.
            multiplier (str): The second number.

        Returns:
            str: The product of multiplicand and multiplier.
        """
        #  return "0" if multiplicand or multiplier are not valid binaries
        if not self.check_binary(multiplicand, multiplier):
            return "0"

        #  change multiplier into a string and reverse it
        multiplier = str(multiplier)[::-1]
        #  create empty variable to store the product
        product = "0"

        #  iterate through each character of multiplier
        for i in range(len(multiplier)):
            #  if character is "1", add multiplicand with zeros to product
            if multiplier[i] == "1":
                product = self.add(str(product), multiplicand + "0" * i)

        #  return product as a string
        return str(product)

    #  define divide function
    def div(self, dividend: str, divisor: str) -> str:
        """
        Divides two binary numbers and returns the quotient.

        Args:
            dividend (str): The first number.
            divisor (str): The second number.

        Returns:
            str: The quotient of dividend and divisor.
        """
        #  return "0" if dividend or divisor are not valid binaries
        if not self.check_binary(dividend, divisor):
            return "0"

        #  return the dividend if divisor is "1"
        if divisor == "1":
            return dividend
        #  return "1" if the divisor is the same as the dividend
        elif divisor == dividend:
            return "1"
        #  return "0" if the divisor is "0" or divisor is longer than dividend
        elif divisor == "0" or len(divisor) > len(dividend):
            return "0"

        #  create empty variable to store the quotient
        quotient = ""
        #  create empty variable to store the length of the dividend
        length = len(dividend)

        #  itereate through each character of dividend from the back
        for i in range(len(dividend) - len(divisor), -1, -1):
            #  create variable to store the divisor with trailing zeros
            div_temp = divisor + "0" * i
            #  create a variable to check if dividend is less than div_temp
            divisible = True
            #  add trailing zeros to dividend if shorter than div_temp
            if len(dividend) < length:
                dividend = "0" * (length - len(dividend)) + dividend
            # add trailing zeros to div_temp if shorter than dividend
            elif len(dividend) > length:
                div_temp = "0" * (len(dividend) - len(div_temp)) + div_temp
            #  iterate through each character of dividend
            for j in range(len(div_temp)):
                #  if character of div_temp is less than character of dividend
                if dividend[j] > div_temp[j]:
                    #  break
                    break
                #  if character of dividend's less than character of div_temp
                elif dividend[j] < div_temp[j]:
                    #  set divisible to False and break
                    divisible = False
                    break

            #  if divisible, append "1" to quotient
            if divisible:
                quotient += "1"
                #  then subtract div_temp from dividend
                dividend = self.subt(dividend, div_temp)
            #  else appedn "0" to quotient
            else:
                quotient += "0"
            #  decrement length by 1
            length -= 1

        #  create variable to store the index of the first "1"
        ones_loc = 0
        #  iterate through each character of quotient
        for i in range(len(quotient)):
            #  if character is "1", set ones_loc to the index and break
            if quotient[i] == "1":
                ones_loc = i
                break

        #  return the quotient with trailing zeros removed
        return quotient[ones_loc:]

    #  define operate function
    def operate(self):
        """
        Coordinates the execution of binary arithmetic methods in Binary.

        Args:

        Returns:

        """
        #  if self.operator is "+", add self.a and self.b
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        #  else if self.operator is "-", subtract self.b from self.a
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        #  else if self.operator is "*", multiply self.a and self.b
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        #  else if self.operator is "/", divide self.a by self.b
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)


#  defining Binary, inheriting from Number
class Binary(Number):

    #  initiate Binary
    def __init__(self, a, b, operator):
        super().__init__(a, b, operator)
        """
        Initialise Binary class.

        Args:
            a: The first number.
            b: The second number.
            operator: The operator.

        Returns:

        """


#  defining Decimal, inheriting from Number
class Decimal(Number):

    #  initiate Decimal
    def __init__(self, a, b, operator):
        #  inherit a, b, and operator from Number
        super().__init__(a, b, operator)
        """
        Initialise Decimal class.

        Args:
            a: The first number.
            b: The second number.
            operator: The operator.

        Returns:

        """
        #  create a variable with all characters of number system
        self.dec_dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        #  check if a is valid, if not, set a = "0"
        if self.check_decimal(a):
            self.a = a
        else:
            self.a = "0"

        #  check if b is valid, if not, set b = "0"
        if self.check_decimal(b):
            self.b = b
        else:
            self.b = "0"

    #  define check_decimal function
    def check_decimal(self, a, b="0") -> bool:
        """
        Checks if arguments are valid decimals and returns a bool.

        Args:
            a: The first number.
            b: The second number (default value: "0").

        Returns:
            bool: The validity of a and b.
        """
        #  convert a into a string if it is of type int
        if isinstance(a, int):
            a = str(a)

        #  convert b into a string if it is of type int
        if isinstance(b, int):
            b = str(b)

        #  return False if a or b are not of type str
        if not isinstance(a, str) or not isinstance(b, str):
            return False

        #  concatinate a and b together
        ab = f"{a}{b}"
        #  return true if all values in ab are in dec_dig, else false
        return all(i in self.dec_dig for i in ab)

    #  define check_operator function
    def dec_to_bin(self, decimal: str) -> str:
        """
        Converts a decimal to binary and returns a string.

        Args:
            decimal (str): The decimal.

        Returns:
            str: The binary equivalent of the decimal.
        """
        #  return "0" if decimal is not valid decimal
        if not self.check_decimal(decimal):
            return "0"

        #  convert decimal into an integer
        decimal = int(decimal)
        #  create a variable to store the ceiling
        ceiling = 0
        #  iterate through each number until decimal
        for i in range(int(decimal)):
            #  if 2 to the power of i is greater than decimal
            if 2**i >= decimal:
                #  set ceiling to i and break
                ceiling = i
                break

        #  create a variable to store the binary
        output = ""
        #  iterate through each number from ceiling to 0
        for i in range(ceiling - 1, -1, -1):
            #  if 2 to the power of i is less than or equal to decimal
            if decimal >= 2**i:
                #  append "1" to output
                output += "1"
                #  minus 2 to the power of i from decimal
                decimal -= 2**i
            #  else append "0" to output
            else:
                output += "0"

        #  return output as a string
        return output

    #  define check_operator function
    def bin_to_dec(self, binary: str) -> str:
        """
        Converts a binary to decimal and returns a string.

        Args:
            binary (str): The binary.

        Returns:
            str: The decimal equivalent of the binary.
        """
        #  return "0" if binary is not valid binary
        if not self.check_binary(binary):
            return "0"

        #  create a variale to store the decimal
        output = 0
        #  convert the binary into a string and reverse it
        binary = str(binary)[::-1]
        #  iterate through each character of binary
        for i in range(len(binary)):
            #  append
            output += int(binary[i]) * (2**i)

        #  return output as a string
        return str(output)

    #  define check_operator function
    def operate(self):
        """
        Coordinates the execution of binary arithmetic methods in Decimal.

        Args:

        Returns:

        """
        #  replace self.a and self.b with the binary equivalent
        self.a = self.dec_to_bin(self.a)
        self.b = self.dec_to_bin(self.b)
        #  if self.operator is "+", add self.a and self.b
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        #  else if self.operator is "-", subtract self.b from self.a
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        #  else if self.operator is "*", multiply self.a and self.b
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        #  else if self.operator is "/", divide self.a by self.b
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)
        #  replace self.result with the decimal equivalent
        self.result = self.bin_to_dec(self.result)


#  defining Hex, inheriting from Number
class Hexadecimal(Number):

    #  initiate Hexadecimal
    def __init__(self, a, b, operator):
        #  inherit a, b, and operator from Number
        super().__init__(a, b, operator)
        #  create a variable with all characters of number system
        self.hex_dig = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C",
            "D", "E", "F"
        ]

        #  check if a is valid, if not, set a = "0"
        if self.check_hexadecimal(a):
            self.a = a
        else:
            self.a = "0"

        #  check if b is valid, if not, set b = "0"
        if self.check_hexadecimal(b):
            self.b = b
        else:
            self.b = "0"

        #  create a variable with all binary equivalents of hex_dig
        self.hex_binaries = [
            "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111",
            "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"
        ]

    #  define check_hexadecimal function
    def check_hexadecimal(self, a, b="0") -> bool:
        """
        Checks if arguments are valid hexadecimals and returns a bool.

        Args:
            a: The first number.
            b: The second number (default value: "0").

        Returns:
            bool: The validity of a and b.
        """
        #  return False if a or b are not of type str
        if not isinstance(a, str) or not isinstance(b, str):
            return False

        #  concatinate a and b together
        ab = f"{a}{b}"
        #  return true if all values in ab are in hex_dig, else false
        return all(i in self.hex_dig for i in ab)

    #  define check_operator function
    def hex_to_bin(self, hexadecimal: str) -> str:
        """
        Converts a hexadecimal to binary and returns a string.

        Args:
            hexadecimal (str): The hexadecimal.

        Returns:
            str: The binary equivalent of the hexadecimal.
        """
        #  return "0" if hexadecimal is not valid hexadecimal
        if not self.check_hexadecimal(hexadecimal):
            return "0"

        #  create variable to store the binary
        output = ""
        #  iterate through each character of hexadecimal
        for i in range(len(hexadecimal)):
            #  itereate through each item of self.hex_dig
            for j in range(len(self.hex_dig)):
                #  if character of hexadecimal is equal to item of self.hex_dig
                if hexadecimal[i] == self.hex_dig[j]:
                    #  append the binary equivalent of the item to output
                    output += self.hex_binaries[j]

        #  create a variable to store the index of the first "1"
        ones_loc = 0
        #  iterate through each character of output
        for i in range(len(output)):
            #  if character is "1", set ones_loc to the index and break
            if output[i] == "1":
                ones_loc = i
                break

        #  return the output with trailing zeros removed
        return output[ones_loc:]

    #  define check_operator function
    def bin_to_hex(self, binary: str) -> str:
        """
        Converts a binary to hexadecimal and returns a string.

        Args:
            binary (str): The binary.

        Returns:
            str: The hexadecimal equivalent of the binary.
        """
        #  return "0" if binary is not valid binary
        if not self.check_binary(binary):
            return "0"

        #  add trailing zeros to binary if shorter than multiple of 4
        binary = "0" * (4 - len(binary) % 4) + binary

        #  create a variable to store the binaries split at every 4 characters
        binary_ls = []
        #  while there is still something in binary
        while binary:
            #  append the first 4 characters to binary_ls
            binary_ls.append(binary[:4])
            #  remove the first 4 characters from binary
            binary = binary[4:]

        #  create a variable to store the hexadecimal
        output = ""
        #  iterate through each binary in binary_ls
        for i in binary_ls:
            #  append the hexadecimal equivalent of binary to output
            output += self.hex_dig[self.hex_binaries.index(i)]

        #  return output as a string
        return output

    def operate(self):
        """
        Coordinates the execution of binary arithmetic methods in Hexadecimal.

        Args:

        Returns:

        """
        #  replace self.a and self.b with the binary equivalent
        self.a = self.hex_to_bin(self.a)
        self.b = self.hex_to_bin(self.b)
        #  if self.operator is "+", add self.a and self.b
        if self.operator == "+":
            self.result = self.add(self.a, self.b)
        #  else if self.operator is "-", subtract self.b from self.a
        elif self.operator == "-":
            self.result = self.subt(self.a, self.b)
        #  else if self.operator is "*", multiply self.a and self.b
        elif self.operator == "*":
            self.result = self.mult(self.a, self.b)
        #  eles if self.operator is "/", divide self.a by self.b
        elif self.operator == "/":
            self.result = self.div(self.a, self.b)
        #  replace self.result with the hexadecimal equivalent
        self.result = self.bin_to_hex(self.result)


#  defining the main function
def main():
    """
    The function that runs the calculator.

    Args:

    Returns:

    """
    #  create a variable to store all number systems
    num_systems = {1: "binary", 2: "decimal", 3: "hexadecimal"}

    #  create a variable to store all possible operations
    operations = {
        "+": "addition",
        "-": "subtraction",
        "*": "multiplication",
        "/": "division"
    }

    #  print welcome message
    print("Welcome to the programmer's calculator")

    #  print instructions
    print("\nInstructons:")
    print("1. Enter two numbers from the same number system.")
    print("2. Enter an operator (+, -, *, /).")
    print("3. Select the number system that your two numbers are in.")
    print("4. The result will be displayed in the number system you selected.")
    #  wait for user input to continue
    input("\nPress enter to continue ")

    #  create three variables to store first, second, and operator
    a = input("\nEnter the first number\n- ").strip().upper()
    b = input("\nEnter the second number\n- ").strip().upper()
    operator = input("\nEnter the operator (+, -, *, /)\n- ").strip()

    #  if operator is not in operations, print error message and exit
    if operator not in operations:
        print("\nInvalid input: Operator must be +, -, *, or /")
        return

    #  create an Binary object with None, None, and None
    test = Binary(None, None, None)
    #  test if a and b are valid for number system
    test_bin = test.check_binary(f"{a}{b}")
    #  delete Binary object
    del test

    #  create a Decimal object with None, None, and None
    test = Decimal(None, None, None)
    #  test if a and b are valid for number system
    test_dec = test.check_decimal(f"{a}{b}")
    #  delete Decimal object
    del test

    #  create a Hexadecimal object with None, None, and None
    test = Hexadecimal(None, None, None)
    #  test if a and b are valid for number system
    test_hex = test.check_hexadecimal(f"{a}{b}")
    #  delete Hexadecimal object
    del test

    #  if test_bin is True, predict number system is binary
    if test_bin:
        num_sys = 1
    #  if test_dec is True, predict number system is decimal
    elif test_dec:
        num_sys = 2
    #  if test_hex is True, predict number system is hexadecimal
    elif test_hex:
        num_sys = 3
    #  else, print error message and exit
    else:
        print("\nInvalid input: A, B must be of valid number system")
        return

    #  ask if predicted number system is correct
    print(f"\nTrying to do {num_systems[num_sys]} {operations[operator]}?")
    correct_num_sys = input("Y/N: ").strip()

    #  if correct_num_sys is not "Y" and there is something in correct_num_sys
    #  ask the user what number system they would like to calculate in
    if correct_num_sys.upper() != "Y" and correct_num_sys:
        print("\nEnter number corresponding to number system to calculate in:")
        num_sys = int(input("1. Binary\n2. Decimal\n3. Hexadecimal\n- "))

        #  if num_sys is not 1, 2, or 3, print error message and exit
        if num_sys not in num_systems:
            print("\nInvalid input: Number system must be 1, 2, or 3")
            return

    #  if num_sys is 1 and test_bin is True
    if num_sys == 1 and test_bin:
        #  create a Binary object with a, b, and operator as arguments
        calc = Binary(a, b, operator)

    #  else if num_sys is 2 and test_dec is True
    elif num_sys == 2 and test_dec:
        #  create a Decimal object with a, b, and operator as arguments
        calc = Decimal(a, b, operator)

    #  else if num_sys is 3 and test_hex is True
    elif num_sys == 3 and test_hex:
        #  create a Hexadecimal object with a, b, and operator as arguments
        calc = Hexadecimal(a, b, operator)

    #  else, print error message and exit
    else:
        print("\nInvalid input: A, B must be valid for selected number system")
        return

    #  calculate
    calc.operate()

    #  print the result
    print(f"\nIn {num_systems[num_sys]}, {a} {operator} {b} = {calc.result}")


#  call main function when python script is run
#  note: importing this file will not run main()
if __name__ == "__main__":
    main()
