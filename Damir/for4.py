price_per_kg = float(input("Введите цену за 1 кг конфет: "))

for kg in range(1, 11):
    cost = price_per_kg * kg
    print(f"{kg} кг конфет стоит {cost:.2f}")