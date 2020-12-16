from db.dal_queries.countries_queries import CountriesQueries
from pydantic import BaseModel

class Religion():
    country: str
    religion: str
    percentage: float
    def __init__(self, record: tuple, country: str):
        # initialize country data
        self.religion = record[0]
        self.percentage = record[1]
        self.country = country