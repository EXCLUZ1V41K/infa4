import math


a = float(input("a = "))
t = float(input("t = "))
D = 9.8 * a ** 2 + 5.52 * math.cos(t ** 5)
print("Ответ:", D)
