from analyzers.dict_analyzer import DictAnalyzer
from db.dal_queries.countries_queries import CountriesQueries
from db.db_handler import DbHandler
from utils.logger_provider import LoggerProvider


class ContinentDictAnalyzer(DictAnalyzer):

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler)
        self.logger = LoggerProvider.get_logger(__name__)

    def analyze_dict(self, raw_data: dict) -> None:
        data = dict()
        try:
            data['country_code'] = self.country_name_to_code.get(raw_data['name'], None)
            if data['country_code'] is None:
                return
            data['continent'] = raw_data['continent']['name']
            self.db_handler.execute(CountriesQueries.UPDATE_COUNTRY_CONTINENT,
                                    (data['continent'], data['country_code']))
        except Exception as e:
            self.logger.error(e)
