from db.dal_queries.countries_queries import CountriesQueries

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
        self.population = record[2]
        self.lat = record[3]
        self.lot = record[4]
