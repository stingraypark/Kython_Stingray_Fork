# Import
from .tokenizer import tokenize
from .yml import read_yml
from .dict_handler import find_key_by_value, merge_two_dicts

# Load data
FUNCTIONS_AND_KEYWORDS = merge_two_dicts(read_yml('data/functions.yml'),
                                         read_yml('data/keywords.yml'))

# Define functions
def interpret_kpy_2_py(code):
    result = ''

    for token_type, code in tokenize(code):
        if token_type == "STRING":
            result += code
        else:
            if code in list(FUNCTIONS_AND_KEYWORDS.values()):
                result += find_key_by_value(FUNCTIONS_AND_KEYWORDS, code)
            else:
                result += code

    return result

def interpret_py_2_kpy(code):
    result = ''

    for token_type, code in tokenize(code):
        if token_type == "STRING":
            result += code
        else:
            if code in list(FUNCTIONS_AND_KEYWORDS.keys()):
                result += FUNCTIONS_AND_KEYWORDS[code]
            else:
                result += code

    return result