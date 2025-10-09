N = int(input("Введите целое число N (> 0): "))
summa = 0.0

for i in range(1, N + 1):
    summa += 1 / i

print("Сумма ряда:", summa)