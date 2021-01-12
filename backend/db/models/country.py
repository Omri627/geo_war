from db.dal_queries.countries_queries import CountriesQueries
from db.business_logic.utils import convert_to_int, convert_to_float

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
        self.area = convert_to_int(record[2])
        self.population = convert_to_int(record[3])
        self.nationality = record[4]
        self.birth_rate = convert_to_float(record[5])
        self.death_rate = convert_to_float(record[6])
        self.cellular_subscriptions = convert_to_int(record[7])
        self.internet_users = convert_to_int(record[8])
        self._0_14_years = convert_to_float(record[9])
        self._15_24_years = convert_to_float(record[10])
        self._25_54_years = convert_to_float(record[11])
        self._55_64_years = convert_to_float(record[12])
        self._65_over = convert_to_float(record[13])
        self.total_median_age = convert_to_float(record[14])
        self.female_median_age = convert_to_float(record[15])
        self.male_median_age = convert_to_float(record[16])
        self.male_expectancy = convert_to_float(record[17])
        self.female_expectancy = convert_to_float(record[18])
        self.total_expectancy = convert_to_float(record[19])
        self.unemployment_rate = convert_to_float(record[21])
        self.revenues = convert_to_int(record[22])
        self.expenditures = convert_to_int(record[23])
        self.imports = convert_to_int(record[24])
        self.exports = convert_to_int(record[25])
        self.continent = record[26]
