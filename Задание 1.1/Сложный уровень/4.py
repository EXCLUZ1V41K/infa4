import math


x = float(input("x = "))
y = float(input("y = "))
F = math.sqrt((2 + y) ** 2 + math.sqrt(math.sin(y + 5)) ** 7) / math.log(x + 1) - y ** 3
print("Ответ:", F)
