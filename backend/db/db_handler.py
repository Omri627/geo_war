from db.db_helper import DbHelper


class DbHandler:
    BULK_SIZE = 10
    COUNTRIES_FILED = (
        'code', 'name', 'area', 'population', 'nationality', 'birth_rate', 'death_rate', 'cellular_subscriptions',
        'internet_users', 'crime_index', 'health_care', 'quality_of_life', 'lat', 'lon',
        '0-14_years', '15-24_years', '25-54_years', '55-64_years', '65_over', 'total_median_age', 'female_median_age',
        'male_median_age', 'male_expectancy', 'female_expectancy', 'total_expectancy', 'gdp', 'unemployment_rate',
        'revenues', 'expenditures', 'imports', 'exports', 'cost_of_living', 'continent')

    def __init__(self):
        self.helper = DbHelper.get_instance()
        self.countries_values_list = list()

    def insert_to_countries_table(self, data: dict) -> None:
        data_tuple = tuple(data.get(filed, None) for filed in self.COUNTRIES_FILED)
        self.countries_values_list.append(data_tuple)
        if len(self.countries_values_list) == self.BULK_SIZE:
            countries_fields = str(self.COUNTRIES_FILED).replace("'", "")
            insert_country_sql = f'INSERT INTO countries {countries_fields} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor = self.helper.db.cursor()
            try:
                cursor.executemany(insert_country_sql, self.countries_values_list)
                self.helper.db.commit()
            except Exception as e:
                print(e)
            # reset value list
            self.countries_values_list = list()

    def flush_to_db(self):
        countries_fields = str(self.COUNTRIES_FILED).replace("'", "")
        insert_country_sql = f"""INSERT INTO countries 
                                            {countries_fields}"
                                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor = self.helper.db.cursor()
        cursor.executemany(insert_country_sql, self.countries_values_list)
        self.helper.db.commit()
        # reset value list
        self.countries_values_list = list()
        # todo: flush method by table

# todo: move the queries to new class
