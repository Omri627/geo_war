from db.dal_queries.countries_queries import CountriesQueries
from db.business_logic.utils import convert_to_float

class Religion():
    country: str
    religion: str
    percentage: float
    def __init__(self, record: tuple, country: str):
        # initialize country data
        self.religion = record[0]
        self.percentage = convert_to_float(record[1])
        self.country = country
