x1 = 5
if (type(x1) is int):
    print("True")
else:
    print("False")

x2 = 5.5
if (type(x2) is not float):
    print("true")
else:
    print("false")

a = 20
b = 20
if (a is b):
    print("x & y SAME identity")
if (a is not b):
    print("x & y have DIFFERENT identity")