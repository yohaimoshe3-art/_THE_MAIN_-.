
def get_statistics(numbers) -> dict:
    my_dict = {
        "numbers" : sum(numbers),
        "avg" : sum(numbers) / len(numbers),
        "min" : min(numbers),
        "max" : max(numbers),
        "length" : len(numbers),
    }
    return my_dict

numbers = [4, 8, 2, 10, 6]

result = get_statistics(numbers)
print(result)
















