from collections import defaultdict
from typing import List

from analyzers.dict_analyzer import DictAnalyzer
from db.db_handler import DbHandler
from utils.logger_provider import LoggerProvider


def _convert_to_full_number(number: float, multi: str) -> int:
    if multi == "million":
        return int(number * 1000000)
    elif multi == "billion":
        return int(number * 1000000000)
    elif multi == "trillion":
        return int(number * 1000000000000)
    else:
        raise NameError(f"Name '{multi}' not supported")


def _extract_phone_subscribes(line: str) -> int:
    subscribes: List[str] = line.split()
    number_str = subscribes[0].replace(",", "")
    if len(subscribes) == 1:
        return int(number_str)
    else:
        return _convert_to_full_number(float(number_str), subscribes[1])


def _extract_filed_might_be_in_dict(data: any, filed: str):
    if isinstance(data, dict):
        if filed in data:
            return data[filed]
    else:
        return data


class CountriesDictAnalyzer(DictAnalyzer):

    def __init__(self, db_handler: DbHandler):
        super().__init__(db_handler)
        self.logger = LoggerProvider.get_logger(__name__)

    def analyze_dict(self, raw_data: dict) -> None:
        try:
            data = dict()
            data['code'] = raw_data['code']
            data['name'] = raw_data['name']
            data['area'] = float(
                _extract_filed_might_be_in_dict(raw_data['geography']['area'], 'total').split()[0].replace(',', ''))
            try:
                data['population'] = int(raw_data['people_and_society']['population'].split()[0].replace(',', ''))
            except Exception as e:
                self.logger.error(f"country code: {data['code']}, Error: {e}")
            try:
                data['nationality'] = raw_data['people_and_society']['nationality']['adjective'].split(",")[0]
            except Exception as e:
                self.logger.error(f"country code: {data['code']}, Error: {e}")
            try:
                data['birth_rate'] = float(raw_data['people_and_society']['birth_rate'].split()[0])
                data['death_rate'] = float(raw_data['people_and_society']['death_rate'].split()[0])
            except Exception as e:
                self.logger.error(f"country code: {data['code']}, Error: {e}")
            try:
                data['cellular_subscriptions'] = _extract_phone_subscribes(
                    raw_data['communications']['telephones_mobile_cellular']['total_subscriptions'])
            except Exception as e:
                self.logger.error(f"country code: {data['code']}, Error: {e}")
            try:
                data['internet_users'] = int(raw_data['communications']['internet_users']['total'].replace(",", ''))
            except Exception as e:
                self.logger.error(f"country code: {data['code']}, Error: {e}")
            try:
                data['0_14_years'] = float(
                    raw_data['people_and_society']['age_structure']['0_14_years'].split()[0][:-1])
                data['15_24_years'] = float(
                    raw_data['people_and_society']['age_structure']['15_24_years'].split()[0][:-1])
                data['25_54_years'] = float(
                    raw_data['people_and_society']['age_structure']['25_54_years'].split()[0][:-1])
                data['55_64_years'] = float(
                    raw_data['people_and_society']['age_structure']['55_64_years'].split()[0][:-1])
                data['65_over'] = float(
                    raw_data['people_and_society']['age_structure']['65_years_and_over'].split()[0][:-1])

                data['total_median_age'] = float(raw_data['people_and_society']['median_age']['total'].split()[0])
                data['female_median_age'] = float(raw_data['people_and_society']['median_age']['female'].split()[0])
                data['male_median_age'] = float(raw_data['people_and_society']['median_age']['male'].split()[0])
                data['total_expectancy'] = float(
                    raw_data['people_and_society']['life_expectancy_at_birth']['total_population'].split()[0])
                data['male_expectancy'] = float(
                    raw_data['people_and_society']['life_expectancy_at_birth']['male'].split()[0])
                data['female_expectancy'] = float(
                    raw_data['people_and_society']['life_expectancy_at_birth']['female'].split()[0])
            except Exception as e:
                self.logger.error(f"country code: {data['code']}, Error: {e}")
            try:
                gdp_raw, multi = list(raw_data['economy']['gdp_purchasing_power_parity'].values())[0].split()
                data['gdp'] = _convert_to_full_number(float(gdp_raw[1:]), multi)
                revenues, multi = raw_data['economy']['budget']['revenues'].split()[:2]
                data['revenues'] = _convert_to_full_number(float(revenues), multi)
                expenditures, multi = raw_data['economy']['budget']['expenditures'].split()[:2]
                data['expenditures'] = _convert_to_full_number(float(expenditures), multi)
                imports, multi = list(raw_data['economy']['imports'].values())[0].split()
                data['imports'] = _convert_to_full_number(float(imports[1:]), multi)
                imports, multi = list(raw_data['economy']['exports'].values())[0].split()
                data['exports'] = _convert_to_full_number(float(imports[1:]), multi)
                data['unemployment_rate'] = float(list(raw_data['economy']['unemployment_rate'].values())[0][:-1])
            except Exception as e:
                self.logger.error(f"country code: {data['code']}, Error: {e}")

            self.db_handler.insert_to_countries_table(data)

        except Exception as e:
            self.logger.error(f"Failed to load, country code: {raw_data['code']}")
            self.logger.error(e)
