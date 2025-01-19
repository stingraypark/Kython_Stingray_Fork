# Define functions
def find_key_by_value(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]

def merge_two_dicts(dictionary_1, dictionary_2):
    result = dictionary_1.copy()
    result.update(dictionary_2)
    return result