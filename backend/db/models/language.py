from db.business_logic.utils import convert_to_float

class Language:
    country: str
    language: str
    percentage: float

    def __init__(self, record: tuple, country: str):
        # initialize language data
        self.language = record[0]
        self.percentage = convert_to_float(record[1])
        self.country = country
