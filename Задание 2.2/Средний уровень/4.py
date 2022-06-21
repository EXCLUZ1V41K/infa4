s = float(input("Введите сумму покупки: "))
if s >= 1000:
    discount = s - s * 0.10
    print("Сумма с учётом скидки", discount)
else:
    print("Скидки не будет")
