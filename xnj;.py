import numpy as np

# Данные о поставщиках и потребителях
supply = np.array([500, 1000, 900])  # Запасы поставщиков: ЕКБ, СПБ, МСК
demand = np.array([1200, 1000, 1000, 1000])  # Потребности потребителей: Омск, Томск, Пермь

# Стоимость транспортировки
cost = np.array([
    [600, 1100, 1000, 900],  # ЕКБ
    [700, 400, 1000, 900],  # СПБ
    [500, 1000, 900, 800]  # МСК
])

allocation = np.zeros(cost.shape)


def least_cost_method(supply, demand, cost):
    supply_remaining = supply.copy()
    demand_remaining = demand.copy()

    for _ in range(len(supply) * len(demand)):
        # Находим минимальную стоимость
        min_cost_index = np.unravel_index(np.argmin(cost), cost.shape)
        i, j = min_cost_index

        # Определяем количество, которое можно отправить
        quantity = min(supply_remaining[i], demand_remaining[j])

        # Обновляем матрицу распределения
        allocation[i, j] = quantity

        # Обновляем остатки поставок и потребностей
        supply_remaining[i] -= quantity
        demand_remaining[j] -= quantity

        # Если поставка исчерпана, исключаем её из рассмотрения
        if supply_remaining[i] == 0:
            cost[i, :] = np.inf

        # Если потребность удовлетворена, исключаем её из рассмотрения
        if demand_remaining[j] == 0:
            cost[:, j] = np.inf

    return allocation


allocation = least_cost_method(supply, demand, cost)

F = np.sum(allocation * cost)

# Вывод результатов
print("Распределение грузов:")
print(allocation)
print(f"Целевая функция F = {F}")




