from random import randint

def get_unique_list_numbers() -> list[int]:
    return [randint(-10, 10) for i in range(15)]



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
