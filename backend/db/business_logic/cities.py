from db.dal_queries.city_queries import CitiesQueries
from db.dal_queries.capitals_queries import CapitalQueries
from db.db_handler import DbHandler

class CitiesData():
    def __init__(self):
        self.db_handler = DbHandler()
    
    # returns detailed information about a praticular city
    def get_city_data(self, city: str):
        return self.db_handler.receive_data(CitesQueries.CITY_DATA, city)

    # returns the number of cities in particular country
    def cities_quantity(self, country: str):
        return self.db_handler.get_count(CitiesQueries.CITIES_IN_COUNTRY, country)

    # returns list of most populated cities of particular country
    def most_populated(self, country: str, quantity: int):
        return self.db_handler.receive_data(CitiesQueries.BIGGEST_CITIES, (country, quantity))
    
    # returns the capital city of a praticular country
    def capital_city(self, country: str):
        records = self.db_handler.receive_data(CapitalQueries.CAPITAL_OF_COUNTRY, country)
        return records[0][0]

    def random_big_city(country: str, top: int):
        cities = self.most_populated(country, top)
        return cities[randint(0, top)][0]

    
