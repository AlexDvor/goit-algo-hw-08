import heapq

"""
Уявіть, що вам на технічному інтерв'ю дають наступну задачу, 
яку треба розв'язати за допомогою купи.

Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати 
по два за раз в один кабель, використовуючи з'єднувачі, у порядку, 
який призведе до найменших витрат. Витрати на з'єднання двох кабелів 
дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання 
всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, 
який мінімізує загальні витрати.
"""


def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0

    heapq.heapify(cable_lengths)  # перетворюємо список у купу
    total_cost = 0

    while len(cable_lengths) > 1:
        # дістати два найкоротших кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # з'єднати їх
        cost = first + second
        total_cost += cost

        # покласти назад у купу
        heapq.heappush(cable_lengths, cost)

    return total_cost


cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати на об'єднання кабелів: {result}")
