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
    def game_countries(self, selected_country: str):
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.COUNTRIES_GAME, ())
        index = -1
        for i, record in enumerate(records):
            if record[0] == selected_country:
                index = i
            countries.append(record[0])
        if index != -1:
            countries[index] = countries[2]
        countries[2] = selected_country
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

    def most_field_continent(self, continent: str, field: str, limit: int):
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.MOST_FIELD_CONTINENT, (field, continent, field, limit))
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

    # receives name of a country and a field
    # returns the rank of the country in terms of given field among the countries in the world
    def rank_field_continent(self, country: str, field: str):
        record = self.db_handler.receive_data(CountriesQueries.RANK_COUNTRY_BY_FIELD_CONTINENT, (country, field, field, country))
        return int(record[0][0]) + 1

    # receives name of a country
    # returns the rank of the country in terms of population density among the countries in the world
    def rank_population_density(self, country: str):
        record = self.db_handler.receive_data(CountriesQueries.RANK_COUNTRY_BY_POPULATION_DENSITY, (country,))
        return int(record[0][0]) + 1

    # receives name of a country
    # returns the number of countries in the continent of the given country
    def country_continent_quantity(self, country: str):
        record = self.db_handler.receive_data(CountriesQueries.COUNTRIES_QUANTITY_CONTINENT, (country,))
        return int(record[0][0]) + 1

    # returns the population density of a given country
    def country_population_density(self, country: str):
        record = self.db_handler.receive_data(CountriesQueries.POPULATION_DENSITY, (country,))
        return float(record[0][0])

    # returns the most populated countries
    def pick_options_countries(self, limit: int):
        field_name = 'gdp'
        countries = []
        records = self.db_handler.receive_data(CountriesQueries.MOST_FIELD, (field_name, field_name, limit))
        for i, record in enumerate(records):
            countries.append(record[0])
        countries[13] = 'Ukraine'
        countries[15] = 'Portugal'
        countries[21] = 'Israel'
        countries[25] = 'Uruguay'
        countries[31] = 'Morocco'
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
