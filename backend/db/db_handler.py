from db.db_helper import DbHelper


class DbHandler:
    BULK_SIZE = 10
    COUNTRIES_FILED = (
        'code', 'name', 'area', 'population', 'nationality', 'birth_rate', 'death_rate', 'cellular_subscriptions',
        '0-14_years', '15-24_years', '25-54_years', '55-64_years', '65_over', 'total_median_age', 'female_median_age',
        'male_median_age', 'total_expectancy', 'male_expectancy', 'female_expectancy', 'gdp', 'revenues',
        'expenditures',
        'imports', 'exports')

    def __init__(self):
        self.helper = DbHelper.get_instance()
        self.countries_values_list = list()

    def insert_to_countries_table(self, data: dict) -> None:
        data_tuple = (data.get(filed, None) for filed in self.COUNTRIES_FILED)
        self.countries_values_list.append(data_tuple)
        if len(self.countries_values_list) == self.BULK_SIZE:
            countries_fields = str(self.COUNTRIES_FILED).replace("'", "")
            insert_country_query = f"""INSERT INTO countries 
                                    {countries_fields}"
                                    "VALUES (%s, %s, %f, %d, %s, %f, %f, %d, %d, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %d, %f, %d, %d, %d, %d, %d, %s)"""
            mycursor = self.helper.db.cursor()
