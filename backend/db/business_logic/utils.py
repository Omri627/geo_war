def rank_top_fact(position: int, real_or_fake: bool):
    if position % 10 == 0:
        if real_or_fake:
            return position + 10
        else:
            return position - 10
    if position < 10:
        if real_or_fake:
            top_position = 10 if position > 5 else 5
        else:
            top_position = 5 if position > 5 else position - 1
    elif real_or_fake:
        top_position = position - (position % 10) + 10
    else:
        top_position = position - (position % 10)
    return top_position

def display_field(field: str):
    return field.replace('_', ' ').strip()

def float_display(value):
    str_value = str(value)
    return str_value[:min(4, len(str_value))]