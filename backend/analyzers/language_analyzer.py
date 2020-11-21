from analyzers.dict_analyzer import DictAnalyzer
from db.db_handler import DbHandler
from utils.logger_provider import LoggerProvider
from utils.str_util import split_field_percentage_line


class LanguageDictAnalyzer(DictAnalyzer):

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler)
        self.logger = LoggerProvider.get_logger(__name__)

    def analyze_dict(self, raw_data: dict) -> None:
        data = dict()
        data['country_code'] = raw_data['code']
        try:
            languages = raw_data['people_and_society']['languages']
            data['language'] = split_field_percentage_line(languages)
            self.db_handler.insert_to_languages_table(data)
        except Exception as e:
            self.logger.warn(e)
