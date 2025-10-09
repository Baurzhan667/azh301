# Ввод двух целых чисел A и B (A < B)
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Список чисел между A и B (не включая A и B), в порядке убывания
numbers = list(range(B - 1, A, -1))

# Вывод чисел
for num in numbers:
    print(num)

# Вывод количества этих чисел
print("Количество чисел:", len(numbers))