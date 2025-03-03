import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int):
    in_range = 1 <= min_value <= max_value <= 1000
    valid = min_value <= quantity <= max_value - min_value + 1

    if not (in_range and valid):
        return []

    result = random.sample(range(min_value, max_value + 1), quantity)

    return sorted(result)

lottery_numbers = get_numbers_ticket(1, 987, 6)
print("Лотерейні числа:", lottery_numbers)
