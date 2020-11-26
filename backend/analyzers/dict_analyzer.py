import json
from abc import ABC

from db.db_handler import DbHandler


class DictAnalyzer(ABC):
    """
    analyze a dictionary and extract specific data from it
    """
    NAME_CODE_PATH = 'utils/name_code.json'

    def __init__(self, db_handler: DbHandler):
        self.db_handler = db_handler
        self.country_name_to_code = {}
        with open(self.NAME_CODE_PATH, 'r') as f:
            self.country_name_to_code = json.load(f)

    def analyze_dict(self, raw_data: dict) -> None:
        raise NotImplementedError
