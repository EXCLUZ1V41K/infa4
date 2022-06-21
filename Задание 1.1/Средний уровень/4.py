import math


w = float(input("w = "))
y = float(input("y = "))
G = (9.33 * w ** 3 + math.sqrt(w)) / (math.log(y + 3.5) + math.sqrt(y))
print("Ответ:", G)
