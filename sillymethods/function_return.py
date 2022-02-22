def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def sub(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b


def mul(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def div(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


age = add(30, 5)
height = sub(78, 4)
weight = mul(90, 2)
iq = div(100, 2)

print("age = %d height = %d weight = %d iq = %d" % (age, height, weight, iq))

