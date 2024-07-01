def predict_ns(a, b):
    try:
        test = Hexadecimal(a, b, "+")
        test.sys_to_num()
        return 1
    except ValueError:
        try:
            test = Binary(a, b, "+")
            test.sys_to_num()
            return 2
        except ValueError:
            return 3

def predict_bs(a, b):
    try:
        test = Binary(a, b)
        test.sys_to_num()
        return 1
    except ValueError:
        try:
            test = Decimal(a, b)
            test.sys_to_num()
            return 2
        except ValueError:
            return 3
            


# binary = works with 0, 1
# hexa = words with 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
# decimal = works with 0, 1, 2, 3, 4, 5, 6, 7, 8, 9



number_systems = {
    1: "hexadecimal",
    2: "binary",
    3: "decimal"
}

operations = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division"
}

input(f"Are you trying to do {operations[operator]} {numer_systems[num_system]}?")