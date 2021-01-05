from db.dal_queries.countries_queries import CountriesQueries
from db.models.country import Country
from db.db_handler import DbHandler

class CountriesData:
    def __init__(self):
        self.db_handler = DbHandler()

    # given countries records extracted from the ser
    @staticmethod
    def records_to_objects(records):
        objects = []
        for record in records:
            objects.append(Country(record))
        return objects

    # returns fifteen random countries to compete in the game
    def game_countries(self):
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.COUNTRIES_GAME, ())
        for i, record in enumerate(records):
            countries.append(record[0])
        return countries

    # returns detailed information about a country
    def country_data(self, country: str):
        record = self.db_handler.receive_data(CountriesQueries.COUNTRY_DATA, (country,))
        if record is None or len(record) == 0:
            return None
        return Country(record[0])
    
    # returns the names of the countries which has the largest values of given field
    def most_field(self, field: str, limit: int):
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.MOST_FIELD, (field, field, limit))
        for record in records:
            countries.append({
                'name': record[0],
                'field_value': record[1]
            })
        return countries
    
    # returns the names of the countries which has the smallest values of given field
    def least_field(self, field: str, limit: int):
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.LEAST_FIELD, (field, field, limit))
        for record in records:
            countries.append({
                'name': record[0],
                'field_value': record[1]
            })
        return countries

    # receives name of a country and a field
    # returns the rank of the country in terms of given field among the countries in the world
    def rank_field(self, country: str, field: str):
        record = self.db_handler.receive_data(CountriesQueries.RANK_COUNTRY_BY_FIELD, (field, field, country))
        return int(record[0][0]) + 1

    # returns the most populated countries
    def top_populated_countries(self, limit: int):
        field_name = 'population'
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.MOST_FIELD, (field_name, field_name, limit))
        for i, record in enumerate(records):
            if i not in [15, 23, 51]:
                countries.append(record[0])
        return countries

    # receives a integer limit value indicating the number of records/countries
    # returns a list largest size countries 
    def largest_area_size(self, limit: int):
        field_name = 'area'
        return self.db_handler.receive_data(CountriesQueries.MOST_FIELD, (field_name, field_name, limit))
    
    # returns the countries that has the highest population density
    def top_population_density(self, limit: int):
        return self.db_handler.receive_data(CountriesQueries.TOP_POPULATION_DENSITY, (limit,))
    
    # returns the countries that has the least population density
    def least_population_density(self, limit: int):
        return self.db_handler.receive_data(CountriesQueries.LEAST_POPULATION_DENSITY, (limit,))
