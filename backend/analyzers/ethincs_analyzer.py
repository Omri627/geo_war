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
            name = _assemble_name(name_percent_list[:-1])
            if "%" in name:
                # spacial case for when there is 2 '%'
                name_percent = name[:name.find('%')].split()
                name = _assemble_name(name_percent[:-1])
                # take percent from last and remove %
                percent = float(name_percent[-1][:-1])
            else:
                # take percent from last and remove %
                percent = float(name_percent_list[-1][:-1])
            res.append({name.strip(): percent})
        except Exception as e:
            print(e)
    return res


def _assemble_name(name_list: List[str]) -> str:
    name = ""
    for part_name in name_list:
        name = f"{name} {part_name}"
    return name


class EthnicsDictAnalyzer(DictAnalyzer):

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler)
        self.logger = LoggerProvider.get_logger(__name__)

    def analyze_dict(self, raw_data: dict) -> None:
        data = dict()
        data['country_code'] = raw_data['code']
        try:
            ethnics = raw_data['people_and_society']['ethnic_groups']
            data['name'] = _split_ethnics(ethnics)
            self.db_handler.insert_to_ethnics_table(data)
        except Exception as e:
            self.logger.warn(e)

