def subt(a, b):
    b = b[::-1]
    b_n = ""
    for i in range(len(b)):
        if b[i] == "0":
            b_n += "1"
        elif b[i] == "1":
            b_n += "0"

    b_n = b_n[::-1]

    b_n = add(b_n, "1")
    return add(a, b_n)

add("100010101", "001010111")