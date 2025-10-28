# Write a function that sorts a list of dictionaries by a given key
def sort_dicts_by_key(dicts, key):
    """
    Sorts a list of dictionaries by a specified key.

    Parameters:
    dicts (list): A list of dictionaries to be sorted.
    key (str): The key in the dictionaries to sort by.

    Returns:
    list: A new list of dictionaries sorted by the specified key.
    """
    return sorted(dicts, key=lambda x: x[key])

# Sample Test Case
sample_data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print("Copilot version:", sort_dicts_by_key(sample_data, "age"))