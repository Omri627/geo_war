from db.business_logic.utils import convert_to_float

class EthnicGroup:
    country: str
    name: str
    percentage: float

    def __init__(self, record: tuple):
        # initialize ethnic group data
        self.country = record[0]
        self.name = record[1]
        self.percentage = convert_to_float(record[2])
