from db.dal_quries.capitals_queires import CapitalQueries
from db.dal_quries.city_queries import CitesQueries
from db.dal_quries.countries_queries import CountriesQueries
from db.dal_quries.ethnics_queries import EthnicsQueries
from db.dal_quries.languages_queries import LanguagesQueries
from db.dal_quries.religions_queries import ReligionsQueries
from db.dal_quries.soccer_queries import SoccerQueries
from db.dal_quries.tables import Tables
from db.db_helper import DbHelper
from utils.logger_provider import LoggerProvider


class DbHandler:
    BULK_SIZE = 10

    def __init__(self):
        self.helper = DbHelper.get_instance()
        self.countries_values_list = list()
        self.ethnics_values_list = list()
        self.languages_values_list = list()
        self.religions_values_list = list()
        self.soccer_values_list = list()
        self.city_values_list = list()
        self.capital_values_list = list()
        self.logger = LoggerProvider.get_logger(__name__)

    def insert_to_countries_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in CountriesQueries.FIELDS)
        self.countries_values_list.append(data_tuple)
        if len(self.countries_values_list) == self.BULK_SIZE:
            cursor = self.helper.db.cursor()
            try:
                self._execute_many(cursor, CountriesQueries.INSERT_QUERY, self.countries_values_list)
            except Exception as e:
                print(e)
            # reset value list
            self.countries_values_list = list()

    def insert_to_ethnics_table(self, data: dict) -> None:
        for ethnic_group in data['name']:
            for name, percent in ethnic_group.items():
                self.ethnics_values_list.append((data['country_code'], name, percent))

        if len(self.ethnics_values_list) >= self.BULK_SIZE:
            cursor = self.helper.db.cursor()
            try:
                self._execute_many(cursor, EthnicsQueries.INSERT_QUERY, self.ethnics_values_list)
            except Exception as e:
                print(e)
            # reset value list
            self.ethnics_values_list = list()

    def insert_to_languages_table(self, data: dict) -> None:
        for language in data['language']:
            for name, percent in language.items():
                self.languages_values_list.append((data['country_code'], name, percent))

        if len(self.languages_values_list) >= self.BULK_SIZE:
            cursor = self.helper.db.cursor()
            try:
                self._execute_many(cursor, LanguagesQueries.INSERT_QUERY, self.languages_values_list)
            except Exception as e:
                print(e)
            # reset value list
            self.languages_values_list = list()

    def insert_to_religions_table(self, data: dict) -> None:
        for religion in data['religions']:
            for name, percent in religion.items():
                if len(name) <= 100:
                    self.religions_values_list.append((data['country_code'], name, percent))

        if len(self.religions_values_list) >= self.BULK_SIZE:
            cursor = self.helper.db.cursor()
            try:
                self._execute_many(cursor, ReligionsQueries.INSERT_QUERY, self.religions_values_list)
            except Exception as e:
                print(e)
            # reset value list
            self.religions_values_list = list()

    def insert_to_soccer_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in SoccerQueries.FIELDS)
        self.soccer_values_list.append(data_tuple)

        if len(self.soccer_values_list) == self.BULK_SIZE:
            cursor = self.helper.db.cursor()
            try:
                self._execute_many(cursor, SoccerQueries.INSERT_QUERY, self.soccer_values_list)
            except Exception as e:
                print(e)
            self.soccer_values_list = list()

    def insert_to_city_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in CitesQueries.FIELDS)
        self.city_values_list.append(data_tuple)

        if len(self.city_values_list) == self.BULK_SIZE:
            self._insert_to_table(CitesQueries.INSERT_QUERY, self.city_values_list)
            self.city_values_list = list()

    def insert_to_capital_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in CapitalQueries.FIELDS)
        self.capital_values_list.append(data_tuple)

        if len(self.capital_values_list) == self.BULK_SIZE:
            self._insert_to_table(CapitalQueries.INSERT_QUERY, self.capital_values_list)
            self.capital_values_list = list()

    def flush_to_db(self, table: Tables):
        cursor = self.helper.db.cursor()

        if table.name == Tables.COUNTRIES_TABLE.name:
            try:
                self._execute_many(cursor, CountriesQueries.INSERT_QUERY, self.countries_values_list)
            except Exception as e:
                self.logger.error(e)
            self.countries_values_list = list()
        elif table.name == Tables.ETHNICS_TABLE.name:
            try:
                self._execute_many(cursor, EthnicsQueries.INSERT_QUERY, self.ethnics_values_list)
            except Exception as e:
                self.logger.error(e)
            self.ethnics_values_list = list()
        elif table.name == Tables.LANGUAGES_TABLE.name:
            try:
                self._execute_many(cursor, LanguagesQueries.INSERT_QUERY, self.languages_values_list)
            except Exception as e:
                self.logger.error(e)
            self.languages_values_list = list()
        elif table.name == Tables.RELIGION_TABLE.name:
            try:
                self._execute_many(cursor, ReligionsQueries.INSERT_QUERY, self.religions_values_list)
            except Exception as e:
                self.logger.error(e)
            self.religions_values_list = list()
        elif table.name == Tables.SOCCER_TABLE.name:
            try:
                self._execute_many(cursor, SoccerQueries.INSERT_QUERY, self.soccer_values_list)
            except Exception as e:
                self.logger.error(e)
            self.soccer_values_list = list()
        elif table.name == Tables.CITY_TABLE.name:
            try:
                self._execute_many(cursor, CitesQueries.INSERT_QUERY, self.city_values_list)
            except Exception as e:
                self.logger.error(e)
            self.city_values_list = list()
        elif table.name == Tables.CAPITAL_TABLE.name:
            try:
                self._execute_many(cursor, CapitalQueries.INSERT_QUERY, self.capital_values_list)
            except Exception as e:
                self.logger.error(e)
            self.capital_values_list = list()

    def _execute_many(self, cursor, insert_query: str, values: list):
        cursor.executemany(insert_query, values)
        self.helper.db.commit()
        self.logger.info(f"Inserted {len(values)} to table")

    def _insert_to_table(self, insert_query: str, values: list):
        cursor = self.helper.db.cursor()
        try:
            self._execute_many(cursor, insert_query, values)
        except Exception as e:
            print(e)
