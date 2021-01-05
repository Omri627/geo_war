from db.dal_queries.city_queries import CitiesQueries
from db.dal_queries.capitals_queries import CapitalQueries
from db.db_handler import DbHandler
from db.models.city import City
import random


class CitiesData():
    def __init__(self):
        self.db_handler = DbHandler()

    # convert cities records extracted from database
    # the method convert the raw data into a object
    @staticmethod
    def records_to_objects(records):
        objects = []
        for record in records:
            objects.append(City(record))
        return objects

    # returns detailed information about a particular city
    def get_city_data(self, city: str):
        return self.db_handler.receive_data(CitiesQueries.CITY_DATA, (city,))

    # returns the number of cities in particular country
    def cities_quantity(self, country: str):
        return self.db_handler.get_count(CitiesQueries.CITIES_IN_COUNTRY, (country,))

    # returns list of most populated cities of particular country
    def most_populated(self, country: str, quantity: int):
        records = self.db_handler.receive_data(CitiesQueries.BIGGEST_CITIES, (country, quantity))
        return self.records_to_objects(records)

    # returns the capital city of a particular country
    def capital_city(self, country: str):
        records = self.db_handler.receive_data(CapitalQueries.CAPITAL_OF_COUNTRY, (country,))
        if records is None or len(records) == 0:
            return None
        return records[0][0]

    # returns a random big city in given country
    def random_big_city(self, country: str, top: int):
        cities = self.most_populated(country, top)
        top = min(len(cities) - 1, top)
        return cities[random.randint(0, top) - 1][0]

    # receives names of two countries denoted as first and second
    # returns a list of cities which their population is bigger or closely in scale
    # to the population size of the other country
    def cities_larger_country(self, first: str, second: str):
        cities = []
        records = self.db_handler.receive_data(CitiesQueries.CITIES_LARGER_COUNTRY, (first, second))
        for record in records:
            cities.append({
                'name': record[0],
                'population': int(record[1]),
                'is_bigger': bool(record[2])
            })
        return cities

    # receives name of a country and
    # returns the position of the most populated city in given country among all the cities in the world
    def position_populated_city(self, country: str):
        return self.db_handler.get_count(CitiesQueries.POSITION_POPULATED_CITY, (country,))