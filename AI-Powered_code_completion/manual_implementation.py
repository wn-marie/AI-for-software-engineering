def sort_dicts_by_key_manual(dicts, key):
    """
    Manually sorts a list of dictionaries by a specified key.

    Parameters:
    dicts (list): A list of dictionaries to be sorted.
    key (str): The key in the dictionaries to sort by.

    Returns:
    list: A new list of dictionaries sorted by the specified key.
    """
    for i in range(len(dicts)):
        for j in range(i + 1, len(dicts)):
            if dicts[i][key] > dicts[j][key]:
                dicts[i], dicts[j] = dicts[j], dicts[i]
    return dicts

# Sample Test Case
sample_data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print("Manual version:", sort_dicts_by_key_manual(sample_data.copy(), "age"))
