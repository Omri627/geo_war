from db.dal_queries.ethnics_queries import EthnicsQueries
from db.db_handler import DbHandler
from db.models.ethnic import EthnicGroup


class EthnicsData():
    def __init__(self):
        self.db_handler = DbHandler()

    @staticmethod
    def records_to_objects(records):
        ethnic_groups = []
        for record in records:
            ethnic_groups.append(EthnicGroup(record=record))
        return ethnic_groups

    # given a name of country,
    # the method returns the official language in this country
    def main_ethnic_group(self, country: str):
        result = self.db_handler.receive_data(EthnicsQueries.MAIN_ETHNIC_COUNTRY, (country,))
        if result is None or len(result) == 0:
            return None
        return EthnicGroup(record=result[0])

    # given a name of a country
    # the method returns the languages spoken in it and it's estimated percentage
    def country_ethnic_groups(self, country: str):
        records = self.db_handler.receive_data(EthnicsQueries.ETHNICS_COUNTRY, (country,))
        return self.records_to_objects(records=records)

    # given two countries denoted as first and second,
    # the method returns all common ethnic groups of two given countries
    def common_ethnics(self, first: str, second: str):
        common_ethnic_groups = []
        result = self.db_handler.receive_data(EthnicsQueries.COMMON_ETHNICS, (first, second))
        for record in result:
            common_ethnic_groups.append({
                'first': EthnicGroup(record=(first, record[0], record[1])),
                'second': EthnicGroup(record=(second, record[0], record[2]))
            })
        return common_ethnic_groups
