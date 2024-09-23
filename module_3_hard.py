def calculate_structure_sum(data_structure):
    total = 0
    for item in data_structure:
        if isinstance(item, int):
            total += item
        elif isinstance(item, str):
            total += len(item)
        elif isinstance(item, tuple) or isinstance(item, list):
            total += calculate_structure_sum(item)
        elif isinstance(item, dict):
            total += sum([calculate_structure_sum([key, value])
            for key, value in item.items()])
        elif isinstance(item, set):
            total += sum([calculate_structure_sum([i])
            for i in item])
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), {(2, 'Urban', ('Urban2', 35))})
]

result = calculate_structure_sum(data_structure)
print(result)
