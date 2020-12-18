from typing import Tuple

from db.dal_queries.capitals_queries import CapitalQueries
from db.dal_queries.city_queries import CitiesQueries
from db.dal_queries.countries_queries import CountriesQueries
from db.dal_queries.ethnics_queries import EthnicsQueries
from db.dal_queries.languages_queries import LanguagesQueries
from db.dal_queries.religions_queries import ReligionsQueries
from db.dal_queries.soccer_queries import SoccerQueries
from db.dal_queries.tables import Tables
from db.db_helper import DbHelper
from utils.logger_provider import LoggerProvider


class DbHandler:
    BULK_SIZE = 1

    def __init__(self):
        self.helper = DbHelper.get_instance()
        self.countries_values_list = list()
        self.ethnics_values_list = list()
        self.languages_values_list = list()
        self.religions_values_list = list()
        self.soccer_values_list = list()
        self.city_values_list = list()
        self.capital_values_list = list()
        self.all_capitals_values_list = list()
        self.logger = LoggerProvider.get_logger(__name__)

    def insert_to_countries_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in CountriesQueries.FIELDS)
        self.countries_values_list.append(data_tuple)
        if len(self.countries_values_list) == self.BULK_SIZE:
            self._insert_many_to_table(CountriesQueries.INSERT_QUERY, self.countries_values_list)
            # reset value list
            self.countries_values_list = list()

    def insert_to_ethnics_table(self, data: dict) -> None:
        for ethnic_group in data['name']:
            for name, percent in ethnic_group.items():
                self.ethnics_values_list.append((data['country_code'], name, percent))

        if len(self.ethnics_values_list) >= self.BULK_SIZE:
            self._insert_many_to_table(EthnicsQueries.INSERT_QUERY, self.ethnics_values_list)
            self.ethnics_values_list = list()

    def insert_to_languages_table(self, data: dict) -> None:
        for language in data['language']:
            for name, percent in language.items():
                self.languages_values_list.append((data['country_code'], name, percent))

        if len(self.languages_values_list) >= self.BULK_SIZE:
            self._insert_many_to_table(LanguagesQueries.INSERT_QUERY, self.languages_values_list)
            self.languages_values_list = list()

    def insert_to_religions_table(self, data: dict) -> None:
        for religion in data['religions']:
            for name, percent in religion.items():
                if len(name) <= 100:
                    self.religions_values_list.append((data['country_code'], name, percent))

        if len(self.religions_values_list) >= self.BULK_SIZE:
            self._insert_many_to_table(ReligionsQueries.INSERT_QUERY, self.religions_values_list)
            self.religions_values_list = list()

    def insert_to_soccer_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in SoccerQueries.FIELDS)
        self.soccer_values_list.append(data_tuple)

        if len(self.soccer_values_list) == self.BULK_SIZE:
            self._insert_many_to_table(SoccerQueries.INSERT_QUERY, self.soccer_values_list)
            self.soccer_values_list = list()

    def insert_to_city_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in CitiesQueries.FIELDS)
        self.city_values_list.append(data_tuple)

        if len(self.city_values_list) == self.BULK_SIZE:
            self._insert_many_to_table(CitiesQueries.INSERT_QUERY, self.city_values_list)
            self.city_values_list = list()

    def insert_to_capital_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in CapitalQueries.FIELDS)
        if data_tuple not in self.all_capitals_values_list and data_tuple not in self.capital_values_list:
            self.capital_values_list.append(data_tuple)
            self.all_capitals_values_list.append(data_tuple)

        if len(self.capital_values_list) == self.BULK_SIZE:
            self._insert_many_to_table(CapitalQueries.INSERT_QUERY, self.capital_values_list)
            self.capital_values_list = list()

    def flush_to_db(self, table: Tables):
        cursor = self.helper.db.cursor()
        try:
            if table.name == Tables.COUNTRIES_TABLE.name:
                self._execute_many(cursor, CountriesQueries.INSERT_QUERY, self.countries_values_list)
                self.countries_values_list = list()
            elif table.name == Tables.ETHNICS_TABLE.name:
                self._execute_many(cursor, EthnicsQueries.INSERT_QUERY, self.ethnics_values_list)
                self.ethnics_values_list = list()
            elif table.name == Tables.LANGUAGES_TABLE.name:
                self._execute_many(cursor, LanguagesQueries.INSERT_QUERY, self.languages_values_list)
                self.languages_values_list = list()
            elif table.name == Tables.RELIGION_TABLE.name:
                self._execute_many(cursor, ReligionsQueries.INSERT_QUERY, self.religions_values_list)
                self.religions_values_list = list()
            elif table.name == Tables.SOCCER_TABLE.name:
                self._execute_many(cursor, SoccerQueries.INSERT_QUERY, self.soccer_values_list)
                self.soccer_values_list = list()
            elif table.name == Tables.CITY_TABLE.name:
                self._execute_many(cursor, CitiesQueries.INSERT_QUERY, self.city_values_list)
                self.city_values_list = list()
            elif table.name == Tables.CAPITAL_TABLE.name:
                self._execute_many(cursor, CapitalQueries.INSERT_QUERY, self.capital_values_list)
                self.capital_values_list = list()
        except Exception as e:
            self.logger.error(e)

    def _execute_many(self, cursor, insert_query: str, values: list):
        cursor.executemany(insert_query, values)
        self.helper.db.commit()
        self.logger.info(f"Inserted {len(values)} to table")

    def _insert_many_to_table(self, insert_query: str, values: list):
        cursor = self.helper.db.cursor()
        try:
            self._execute_many(cursor, insert_query, values)
        except Exception as e:
            print(e)

    def insert_one_to_table(self, fields: Tuple[str], insert_query: str, data: dict):
        """
        :param fields: fields in the table
        :param insert_query: full insertion query
        :param data: dict of fields and
        :return:
        """
        data_tuple = tuple(data.get(filed, None) for filed in fields)
        cursor = self.helper.db.cursor()
        cursor.execute(insert_query, data_tuple)
        self.helper.db.commit()

    def receive_data(self, query: str, values: tuple):
        cursor = self.helper.db.cursor()
        cursor.execute(query % values)
        result = cursor.fetchall()
        return result

    def get_count(self, query: str, values: tuple):
        cursor = self.helper.db.cursor()
        cursor.execute(query % values)
        result = cursor.fetchone()
        return int(result[0])

    def execute(self, query: str, values: tuple):
        """
        execute insert or update one row
        """
        final_query = query % values
        cursor = self.helper.db.cursor()
        cursor.execute(final_query)
        self.helper.db.commit()

