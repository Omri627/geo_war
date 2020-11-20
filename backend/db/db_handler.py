from db.dal_quries.countries_queries import CountriesQueries
from db.dal_quries.ethnics_queries import EthnicsQueries
from db.dal_quries.tables import Tables
from db.db_helper import DbHelper
from utils.logger_provider import LoggerProvider


class DbHandler:
    BULK_SIZE = 10

    def __init__(self):
        self.helper = DbHelper.get_instance()
        self.countries_values_list = list()
        self.ethnics_values_list = list()
        self.logger = LoggerProvider.get_logger(__name__)

    def insert_to_countries_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in CountriesQueries.COUNTRIES_FIELDS)
        self.countries_values_list.append(data_tuple)
        if len(self.countries_values_list) == self.BULK_SIZE:
            cursor = self.helper.db.cursor()
            try:
                cursor.executemany(CountriesQueries.INSERT_QUERY, self.countries_values_list)
                self.helper.db.commit()
                self.logger.info(f"Inserted {self.BULK_SIZE} rows to countries table")
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
                cursor.executemany(EthnicsQueries.INSERT_QUERY, self.ethnics_values_list)
                self.helper.db.commit()
                self.logger.info(f"Inserted {len(self.ethnics_values_list)} rows to ethnics table")
            except Exception as e:
                print(e)
            # reset value list
            self.ethnics_values_list = list()

    def flush_to_db(self, table: Tables):
        cursor = self.helper.db.cursor()
        if table.name == Tables.COUNTRIES_TABLE.name:
            try:
                cursor.executemany(CountriesQueries.INSERT_QUERY, self.countries_values_list)
                self.helper.db.commit()
                self.logger.info(f"Inserted {len(self.countries_values_list)} rows to {Tables.COUNTRIES_TABLE.name}")
            except Exception as e:
                self.logger.error(e)
            self.countries_values_list = list()
        elif table.name == Tables.ETHNICS_TABLE.name:
            try:
                cursor.executemany(EthnicsQueries.INSERT_QUERY, self.ethnics_values_list)
                self.helper.db.commit()
                self.logger.info(f"Inserted {len(self.ethnics_values_list)} rows to {Tables.ETHNICS_TABLE.name}")
            except Exception as e:
                self.logger.error(e)
            self.ethnics_values_list = list()

        # reset value list
        self.countries_values_list = list()
