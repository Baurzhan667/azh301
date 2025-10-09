price_per_kg = float(input("Введите цену за 1 кг конфет: "))

for i in range(1, 11):
    weight = i * 0.1
    cost = price_per_kg * weight
    print(f"{weight:.1f} кг конфет стоит {cost:.2f} тенге.")