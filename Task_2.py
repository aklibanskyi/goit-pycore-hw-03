import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (min <= quantity <= max):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(list(numbers))

#Приклад використання
print(get_numbers_ticket(1, 49, 6))
