from typing import List

from analyzers.dict_analyzer import DictAnalyzer
from db.db_handler import DbHandler
from utils.logger_provider import LoggerProvider


def _split_ethnics(ethnics: str) -> List[dict]:
    # give up other ethnic group
    ethnics_with_number = ethnics.split(",")[:-1]
    if 'other' in ethnics_with_number[-1]:
        # spacial case when other is including comma
        ethnics_with_number = ethnics_with_number[:-1]
    res = list()
    for name_percent in ethnics_with_number:
        try:
            name_percent_list = name_percent.split()
            name = ""
            for part_name in name_percent_list[:-1]:
                name = f"{name} {part_name}"
            # take percent from last and remove %
            percent = float(name_percent_list[-1][:-1])
            res.append({name: percent})
        except Exception as e:
            print(e)
    return res


class EthnicsDictAnalyzer(DictAnalyzer):

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler)
        self.logger = LoggerProvider.get_logger(__name__)

    def analyze_dict(self, raw_data: dict) -> None:
        data = dict()
        data['code'] = raw_data['code']
        ethnics = raw_data['people_and_society']['ethnic_groups']
        data['name'] = _split_ethnics(ethnics)
