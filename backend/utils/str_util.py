from typing import List


def split_field_percentage_line(features: str) -> List[dict]:
    # give up other group
    feature_with_number = features.split(",")[:-1]
    if 'other' in feature_with_number[-1]:
        # spacial case when other is including comma
        feature_with_number = feature_with_number[:-1]
    res = list()
    for name_percent in feature_with_number:
        try:
            name_percent_list = name_percent.split()
            name = _assemble_name(name_percent_list[:-1])
            if "%" in name:
                # spacial case for when there is 2 '%'
                name_percent = name[:name.find('%')].split()
                name = _assemble_name(name_percent[:-1])
                # take percent from last and remove %
                percent = float(name_percent[-1][:-1])
            else:
                # take percent from last and remove %
                percent = float(name_percent_list[-1][:-1])
            res.append({name.strip(): percent})
        except Exception as e:
            print(e)
    return res


def _assemble_name(name_list: List[str]) -> str:
    name = ""
    for part_name in name_list:
        name = f"{name} {part_name}"
    return name
