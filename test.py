chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

print(chars[:2])

binary = "1101101"
not_binary = "rj3o E201"

for i in range(len(chars[:2])):
    binary = binary.replace(chars[i], "")
    not_binary = not_binary.replace(chars[i], "")

print(f"binary: {binary}")
print(f"not_binary: {not_binary}")

decimal = "69"
not_decimal = "338dbr9"

for i in range(len(chars[:10])):
    decimal = decimal.replace(chars[i], "")
    not_decimal = not_decimal.replace(chars[i], "")

print(f"decimal: {decimal}")
print(f"not_decimal: {not_decimal}")

hexadecimal = "4D2"
not_hexadecimal = "3oebf"

for i in range(len(chars[:16])):
    hexadecimal = hexadecimal.replace(chars[i], "")
    not_hexadecimal = not_hexadecimal.replace(chars[i], "")

print(f"hexadecimal: {hexadecimal}")
print(f"not_hexadecimal: {not_hexadecimal}")