import random
def rank_top_fact(position: int, real_or_fake: bool):
    ranks = [5, 10, 25, 50, 75, 100, 125, 150, 200, 250, 300, 400, 500]
    if position > 500:
        return position + 100 if real_or_fake else 400
    if position <= 5:
        return position + 1 if real_or_fake else position - 1
    index = len(ranks)
    for i, rank in enumerate(ranks):
        if rank >= position:
            index = i
            break
    if real_or_fake:
        if ranks[index] == position:
            index += 1
        selected_index = random.randint(index, min(index + 3, len(ranks) - 1))
    else:
        selected_index = random.randint(max(0, index - 3), index - 1)
    return ranks[selected_index]

def display_field(field: str):
    return field.replace('_', ' ').strip()

def float_display(value):
    str_value = str(value)
    end = min(str_value.index('.') + 2, len(str_value))
    return str_value[:end]

def convert_to_float(variable):
    if variable is None:
        return -1
    return float(variable)

def convert_to_int(variable):
    if variable is None:
        return -1
    return int(variable)