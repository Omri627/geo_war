from db.dal_queries.countries_queries import CountriesQueries
from db.models.country import Country
from db.db_handler import DbHandler

class CountriesData:
    def __init__(self):
        self.db_handler = DbHandler()
    
    # returns fifteen random countries to compete in the game
    def game_countries(self):
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.COUNTRIES_GAME, ())
        for i, record in enumerate(records):
            countries.append(record[0])
        return countries

    # returns detailed information about a country
    def country_data(self, country: str):
        record = self.db_handler.receive_data(CountriesQueries.COUNTRY_DATA, country)
        return Country(record[0])
    
    # returns the names of the countries which has the largest values of given field
    def most_field(self, country: str, field: str, limit: int):
        return self.db_handler.receive_data(CountriesQueries.MOST_FIELD, (field, limit))
    
    # returns the names of the countries which has the smallest values of given field
    def least_field(self, country: str, field: str, limit: int):
        return self.db_handler.receive_data(CountriesData.LEAST_FIELD, (field, limit))
    
    def most_populated(self, country: str):
        records = self.db_handler.receive_data(CountriesQueries.MOST_FIELD, ('population', limit))
        return records[0]

    # returns the most populated countries
    def top_populated_cities(self, limit: int):
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.MOST_FIELD, ('population', limit))
        for i, record in enumerate(records):
            if i not in [ 15, 23, 51 ]:
                countries.append(record[0])
        return countries

    # receives a integer limit value indicating the number of records/countries
    # returns a list largest size countries 
    def largest_area_size(self, limit: int):
        return self.db_handler.receive_data(CountriesQueries.MOST_FIELD, ('area', limit))
    
    # returns the countries that has the highest population density
    def top_population_density(self, limit: int):
        return self.db.handler.receive_data(CountriesData.TOP_POPULATION_DENSITY, limit)
    
    # returns the countries that has the least population density
    def least_population_density(self, limit: int):
        return self.db.handler.receive_data(CountriesData.LEAST_POPULATION_DENSITY, limit)
    
    # receives name of a country and
    # returns the position of the most populated city in given country among all the cities in the world
    def position_populated_city(self, country: str):
        return self.db.handler.receive_data(CountriesData.POSITION_POPULATED_CITY, country)
    
    # receives name of a country and a field
    # returns the rank of the country in terms of given field among the countries in the world
    def rank_field(self, country: str, field: str):
        return self.db.handler.receive_data(CountriesData.RANK_COUNTRY_BY_FIELD, (field, field, country))

    # receives names of two countries denoted as first and second
    # returns the names of the cities in given first country which has more (or close) population to the population size of entire second given country 
    def cities_larger_country(self, first: str, second: str):
        return self.db.handler.receive_data(CountriesData.CITIES_LARGER_COUNTRY, (first, second))
