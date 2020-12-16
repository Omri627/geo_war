from db.dal_queries.countries_queries import CountriesQueries
from db.dal_queries.religions_queries import ReligionsQueries
from db.models.country import Country
from db.models.religion import Religion
from db.db_handler import DbHandler

class ReligionsData():
    def __init__(self):
        self.db_handler = DbHandler()
    
    # returns list of religions exist in partiuclar country
    def get_country_religions(self, country: str):
        religions = []
        records = self.db_handler.receive_data(ReligionsQueries.COUNTRY_RELIGIONS, country)
        for record in records:
            religions.append(Religion(record=record, country=country))
        return religions

    # returns the most common religion in particular country
    def main_religion(self, country: str):
        records = self.db_handler.receive_data(ReligionsQueries.MOST_COMMON_COUNTRY_RELIGION, country)
        religion = Religion(record=record, country=country)
        return religion

    
