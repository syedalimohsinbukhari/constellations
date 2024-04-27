"""Created on Mar 25 23:51:16 2024."""


def create_star_dictionary(names):
    star_names = {idx: name for idx, name in enumerate(names)}
    return star_names

def create_reverse_mapping(mapping):
    return {value: key for key, value in mapping.items()}

def get_reverse_map(letter_pairs, mapping):
    reverse_mapping = create_reverse_mapping(mapping)
    result = []
    for pair in letter_pairs:
        indices = tuple(reverse_mapping[letter] for letter in pair)
        result.append(indices)
    return result