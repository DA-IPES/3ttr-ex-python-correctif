a = 5
b = 2
print(False and (a >= b))  # False
print(a == b or a != b)  # True
print(a <= 3 <= b)  # False
print(b <= 3 <= a)  # True
print((b <= 3 <= a) and (a != b))  # True
print(a == "5")  # False
