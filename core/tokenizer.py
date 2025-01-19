# Import
import re

# Define functions
def tokenize(code):
    # Define regex patterns
    string_pattern = r'(\"\"\".*?\"\"\"|\'\'\'.*?\'\'\'|\".*?\"|\'.*?\')'
    nonstring_pattern = r'[^\"\']+'
    combined_pattern = f'({string_pattern}|{nonstring_pattern})'

    # Find all match
    tokens = re.findall(combined_pattern, code, re.DOTALL)

    # Classify token
    classified_tokens = []
    for token in tokens:
        # Extract token
        token = token[0] if isinstance(token, tuple) else token
        if re.match(string_pattern, token, re.DOTALL):
            classified_tokens.append(('STRING', token))
        else:
            # Split NONSTRING
            sub_tokens = re.split(r'(\s+|\n|\()', token)
            for sub_token in sub_tokens:
                classified_tokens.append(('NONSTRING', sub_token))

    return classified_tokens