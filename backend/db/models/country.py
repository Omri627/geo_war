from db.dal_queries.countries_queries import CountriesQueries

class Country():
    code: str
    name: str
    area: int
    population: int
    nationality: str
    birth_rate: float
    death_rate: float
    cellular_subscriptions: int
    internet_users: int
    _0_14_years: int
    _15_24_years: int
    _25_54_years: int
    _55_64_years: int
    _65_over: int
    total_median_age: float
    female_median_age: float
    male_median_age:float
    male_expectancy:float
    female_expectancy: float
    total_expectancy: float
    unemployment_rate: float
    revenues: int
    expenditures: int
    imports: int
    exports: int
    continent: str

    def __init__(self, record: tuple):
        # initialize country data
        self.code = record[0]
        self.name = record[1]
        self.area = int(record[2])
        self.population = int(record[3])
        self.nationality = record[4]
        self.birth_rate = record[5]
        self.death_rate = record[6]
        self.cellular_subscriptions = int(record[7])
        self.internet_users = int(record[8])
        self._0_14_years = record[12]
        self._15_24_years = record[13]
        self._25_54_years = record[14]
        self._55_64_years = record[15]
        self._65_over = record[16]
        self.total_median_age = record[17]
        self.female_median_age = record[18]
        self.male_median_age = record[19]
        self.male_expectancy = record[20]
        self.female_expectancy = float(record[21])
        self.total_expectancy = float(record[22])
        self.unemployment_rate = float(record[24])
        self.revenues = record[25]
        self.expenditures = record[26]
        self.imports = record[27]
        self.exports = record[28]
        self.continent = record[30]
