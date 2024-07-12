from binary import Binary
from decimal import Decimal
from hexadecimal import Hexadecimal


num_systems = {
    1: "binary",
    2: "decimal",
    3: "hexadecimal"
}

operations = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division"
}

# test binary, then test decimal, then test hexadecimal

# def predict_num_system(a, b):
#     try:
#         test = Binary(a, b, None)
#         test.sys_to_num()
#         return 1
#     except ValueError:
#         try:
#             test = Decimal(a, b, None)
#             test.sys_to_num()
#             return 2
#         except ValueError:
#             return 3


def main():
    print("Welcome to the programmer calculator.")

    print("Enter the first number:")
    a = input().strip()

    print("Enter the second number:")
    b = input().strip()

    print("Enter the operator: (+, -, *, /)")
    operator = input().strip()

    num_system = predict_ns(a, b)
    print(
        f"Are you trying to do {num_systems[num_system]} {operations[operator]}?"
    )
    predicted_ns = input("Y/N: ")

    if predicted_ns.upper() != "Y":
        print("Enter the number system you want to use:")
        print("1. Binary\n2. Decimal\n3. Hexadecimal")
        num_system = int(input())

    if num_system == 1:
        myclass = Binary(a, b, operator)
        myclass.sys_to_num()
        myclass.operation()
        myclass.num_to_bin()

    elif num_system == 2:
        myclass = Decimal(a, b, operator)
        myclass.sys_to_num()
        myclass.operation()
        myclass.num_to_dec()

    elif num_system == 3:
        myclass = Hexadecimal(a, b, operator)
        myclass.sys_to_num()
        myclass.operation()
        myclass.num_to_hexa()

    else:
        return

    print(
        f"\nIn {num_systems[num_system]}, {a} {operator} {b} is:\n{myclass.fetch_output()}"
    )



if __name__ == "__main__":
    main()