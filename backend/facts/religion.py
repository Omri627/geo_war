from db.business_logic.countries import CountriesData
from db.business_logic.religions import ReligionsData
from random import seed
from random import randint



def more_common_religion(country: str, real_or_fake: bool):
    religions_data = ReligionsData()
    religions = religions_data.get_country_religions(country)
    second_religion = randint(1, len(religions) - 1)
    first_religion = randint(0, second_religion - 1)
    if not real_or_fake:
        first_religion, second_religion = second_religion, first_religion
    return {
        'topic': 'Religion', 
        'fact': 'The religion ' + religions[first_religion].religion + ' is more common then ' + religions[second_religion].religion + ' in the country ' + country,
        'hint': 'The estimated percentage of religion ' + religions[second_religion].religion + ' in the country ' + country + ' is ' + str(religions[second_religion].percentage),
        'answer': real_or_fake,
        'details': 'The estimated percentage of religion ' + religions[first_religion].religion + ' in the country ' + country + ' is ' + str(religions[first_religion].percentage) + 
        ' whereas the estimated percentage of religion ' + religions[second_religion].religion + ' in the country ' + country + ' is ' + str(religions[second_religion].percentage),
    }

def is_common(country: str, real_or_fake: str):
    religions_data = ReligionsData()
    religions = religions_data.get_country_religions(country)
    religion = religions[randint(0, len(religions) - 1)]
    return {
        'topic': 'Religion', 
        'fact': 'The religion ' + religion.religion + ' is common in israel. (common means there is non-zero percentage of people that pursue this religion in the country)',
        'hint': '',
        'answer': real_or_fake,
        'details': 'The estimated percentage of religion ' + religion.religion + ' in the country ' + country + ' is ' + str(religion.percentage),
    }

def above_percentage(country: str, real_or_fake: bool):
    religions_data = ReligionsData()
    religions = religions_data.get_country_religions(country)
    religion = religions[randint(0, len(religions) - 1)]
    
    fact_percentage = int(religion.percentage)
    if fact_percentage > 9:
        fact_percentage = fact_percentage - (fact_percentage % 10)
        if not real_or_fake:
            fact_percentage += 10
    else:
        fact_percentage = 10 if fact_percentage >= 5 else 5
    return {
        'topic': 'Religion', 
        'fact': 'The chance to run into a person who is practising the religion ' + religion.religion + ' is above ' + str(fact_percentage) + '%',
        'hint': '',
        'answer': real_or_fake,
        'details': 'The estimated percentage of people practising the religion ' + religion.religion + ' in the country ' + country + ' is ' + str(religion.percentage) + '%',
    }