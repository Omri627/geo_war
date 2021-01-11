from db.dal_queries.countries_queries import CountriesQueries
from db.business_logic.utils import convert_to_int, convert_to_float

class City():
    name: str
    country: str
    population: int
    lat: float
    lot: float
    def __init__(self, record: tuple):
        # initialize country data
        self.country = record[0]
        self.name = record[1]
        self.population = convert_to_int(record[2])
        self.lat = convert_to_float(record[3])
        self.lot = convert_to_float(record[4])
