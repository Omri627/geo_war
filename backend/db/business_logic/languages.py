from db.dal_queries.languages_queries import LanguagesQueries
from db.db_handler import DbHandler
from db.models.language import Language

class LanguageData():
    def __init__(self):
        self.db_handler = DbHandler()
    
    # given a name of country,
    # the method returns the official language in this country
    def official_language(self, country: str):
        result = self.db_handler.receive_data(LanguagesQueries.OFFICIAL_LANGUAGE, (country,))
        return Language(record=result[0], country=country)
    
    # given a name of a country
    # the method returns the languages spoken in it and it's estimated percentage
    def country_languages(self, country: str):
        languages = []
        result = self.db_handler.receive_data(LanguagesQueries.LANGUAGES_COUNTRY, (country,))
        for record in result:
            languages.append(Language(record=record, country=country))
        return languages
    '''
    # given two countries denoted as first and second,
    # the method returns all common languages of two given countries
    def common_languages(self, first: str, second: str):
        languages = []
        result = self.db_handler.receive_data(LanguagesQueries.LANGUAGES_COUNTRY, (first, second))
        for record in result:
            languages.append((Language(record=(result[0], first, result[1]), country=country), Language(record=(result[0], second, result[2]), country=country))
        return languages
    '''