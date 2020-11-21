from typing import List

from analyzers.dict_analyzer import DictAnalyzer
from db.db_handler import DbHandler
from readers.json_reader import JsonReader
from utils.logger_provider import LoggerProvider


def _substitute_nationality(nationality: str) -> str:
    subs = {
        "England": "United Kingdom",
        "Wales": "United Kingdom",
        "Scotland": "United Kingdom",
        "Northern Ireland": "United Kingdom",
        "China PR": "China",
        "Republic of Ireland": "Ireland",
        "Korea Republic": "Korea, North",
        "Korea DPR": "Korea, South",
        "lbania": "Albania",
        "Congo": "Congo, Republic of the",
        "DR Congo": "Congo, Democratic Republic of the",
        "Gambia": "Gambia, The",
        "Trinidad & Tobago": "Trinidad and Tobago",
        "Antigua & Barbuda": "Antigua and Barbuda",
        "Bosnia & Herzegovina": "Bosnia and Herzegovina",
        "Guinea Bissau": "Guinea-Bissau",
        "Ivory Coast": "Cote d&#39;Ivoire",
        "St Kitts Nevis": "Saint Kitts and Nevis",
        "Czech Republic": "Czechia",
        "Central African Rep.": "Central African Republic",
        "Ermenia": "Armenia",
        "Cape Verde": "Cabo Verde",
        "Namibia": "Cabo Verde",
        "São Tomé & Príncipe": "Sao Tome and Principe",
        "Chinese Taipei": "Taiwan",
        "St Lucia": "Saint Lucia",

    }
    return subs.get(nationality, nationality)


class SoccerListDictAnalyzer(DictAnalyzer):

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler)
        self.logger = LoggerProvider.get_logger(__name__)

    def analyze_dict(self, raw_data: List[dict]) -> None:
        country_code_dict = JsonReader().read_file('utils/name_code.json')
        for row_dict in raw_data:
            data = dict()
            data['country_code'] = country_code_dict.get(_substitute_nationality(row_dict['nationality']), None)
            if data['country_code'] is None:
                self.logger.warn(f"country code not found for: {row_dict['nationality']}")
                continue
            data['player_name'] = row_dict['name']
            data['team'] = row_dict['team'].strip()
            data['position'] = row_dict['position']
            self.db_handler.insert_to_soccer_table(data)
