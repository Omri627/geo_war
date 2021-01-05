from db.dal_queries.countries_queries import CountriesQueries
from db.dal_queries.religions_queries import ReligionsQueries
from db.models.country import Country
from db.models.religion import Religion
from db.db_handler import DbHandler

class ReligionsData():
    def __init__(self):
        self.db_handler = DbHandler()
        self.invalid_religions = [
            'none', 'None', 'non-believer', 'other'
        ]
    
    # returns list of religions exist in praticular country
    def get_country_religions(self, country: str):
        religions = []
        records = self.db_handler.receive_data(ReligionsQueries.COUNTRY_RELIGIONS, (country,))
        for record in records:
            religions.append(Religion(record=record, country=country))
        return religions

    # returns the most common religion in particular country
    def main_religion(self, country: str):
        records = self.db_handler.receive_data(ReligionsQueries.MOST_COMMON_COUNTRY_RELIGION, (country,))
        if records is None or len(records) == 0:
            return None
        religion = Religion(record=records[0], country=country)
        return religion

    # given two countries denoted as first and second,
    # the method returns all common ethnic groups of two given countries
    def common_religions(self, first: str, second: str):
        common_religions = []
        result = self.db_handler.receive_data(ReligionsQueries.COMMON_COUNTRIES_RELIGIONS, (first, second))
        for record in result:
            common_religions.append({
                'first': Religion(record=(record[0], record[1]), country=first),
                'second': Religion(record=(record[0], record[2]), country=second)
            })
        return common_religions

    # return whether the given religion is invalid or not
    def is_invalid_religion(self, religion_name):
        if religion_name in self.invalid_religions:
            return True
        return False
