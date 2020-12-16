from db.dal_queries.countries_queries import CountriesQueries
from pydantic import BaseModel

class Language():
    country: str
    language: str
    percentage: float
    def __init__(self, record: tuple, country: str):
        # initialize language data
        self.language = record[0]
        self.percentage = record[1]
        self.country = country