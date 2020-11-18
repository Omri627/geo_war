from abc import ABC

from db.db_handler import DbHandler


class DictAnalyzer(ABC):
    """
    analyze a dictionary and extract specific data from it
    """

    def __init__(self, db_handler: DbHandler = None):
        self._db_handler = db_handler

    def analyze_dict(self, raw_data: dict) -> None:
        raise NotImplementedError
