import math


x = 2.7
t = -6
b = math.sqrt(x ** 2 + t ** 2)
a = math.log(x)
y = math.sqrt(abs(a - b * x)) ** 5
print("Ответ:", y)
