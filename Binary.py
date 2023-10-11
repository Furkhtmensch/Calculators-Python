def binarySum(a = 0, b = 0):
    a = list("0"*abs(len(a) - len(b))*(len(a) < len(b)) + a)[::-1]
    b = list("0"*abs(len(a) - len(b))*(len(a) > len(b)) + b)[::-1]
    c = ""
    carry = "0"
    for i in range(len(a)):
        if a[i] != carry:
            a[i] = "1"
            carry = "0"
        elif a[i] == carry == "1":
            a[i] = "0"
        if a[i] != b[i]:
            c += "1"
        elif a[i] == b[i] == "1":
            c += "0"
            carry = "1"
        else:
            c += "0"
    if carry == "1":
        c += "1"
    return c[::-1]