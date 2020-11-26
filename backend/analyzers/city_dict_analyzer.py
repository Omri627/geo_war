from analyzers.dict_analyzer import DictAnalyzer
from db.db_handler import DbHandler
from utils.logger_provider import LoggerProvider


class CityDictAnalyzer(DictAnalyzer):

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler)
        self.logger = LoggerProvider.get_logger(__name__)

    def analyze_dict(self, raw_data: dict) -> None:
        data = dict()
        try:
            data['code'] = self.country_name_to_code.get(raw_data['country']['name'], None)
            if data['code'] is None:
                return
            data['name'] = raw_data['name']
            data['population'] = raw_data['population']
            data['lat'] = raw_data['location']['latitude']
            data['lot'] = raw_data['location']['longitude']
            self.db_handler.insert_to_city_table(data)
        except Exception as e:
            self.logger.error(f"Failed to load, raw_data: {raw_data}")
            self.logger.error(e)
