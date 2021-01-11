from db.business_logic.countries import CountriesData
from db.business_logic.religions import ReligionsData
from random import randint


# more_common_religion
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming certain random religion is more common then another religion in country X
# the player should determine whether it is true or false
def more_common_religion(country: str, real_or_fake: bool):
    # get random religions
    religions_data = ReligionsData()
    religions = religions_data.get_country_religions(country)
    if religions is None or len(religions) < 2:
        return None
    if country == 'Germany':
        return None

    second_religion = randint(1, len(religions) - 1)
    first_religion = randint(0, second_religion - 1)
    if not real_or_fake:
        first_religion, second_religion = second_religion, first_religion
    if religions_data.is_invalid_religion(religions[first_religion].religion) or \
            religions_data.is_invalid_religion(religions[second_religion].religion):
        return None

    return {
        'topic': 'Religion', 
        'fact': 'The religion ' + religions[first_religion].religion + ' is more common then ' +
                religions[second_religion].religion + ' in the country ' + country,
        'hint': 'The estimated percentage of religion ' + religions[second_religion].religion +
                ' in the country ' + country + ' is ' + str(religions[second_religion].percentage) + '%',
        'answer': real_or_fake,
        'detail': 'The approximated percentage of religion ' + religions[first_religion].religion +
                   ' in the country ' + country + ' is ' + str(religions[first_religion].percentage) + '%' +
        ' whereas the estimated percentage of religion ' + religions[second_religion].religion +
                   ' in the country ' + country + ' is ' + str(religions[second_religion].percentage) + '%',
    }

# above_percentage
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming certain random religion is The chance to run into a person from
# certain religion is above X% - the player should determine whether it is true or false
def religion_above_percentage(country: str, real_or_fake: bool):
    # get a random religion
    religions_data = ReligionsData()
    religions = religions_data.get_country_religions(country)
    if religions is None or len(religions) == 0:
        return None
    if country == 'Germany':
        return None

    religion_position = randint(0, len(religions) - 1)
    religion = religions[religion_position]
    if religions_data.is_invalid_religion(religion.religion):
        return None

    # compute the percentage appeared in the fact
    fact_percentage = int(religion.percentage)
    if fact_percentage > 9:
        fact_percentage = fact_percentage - (fact_percentage % 10)
        if not real_or_fake:
            fact_percentage += 10
    else:
        fact_percentage = 10 if fact_percentage >= 5 else 5
    return {
        'topic': 'Religion',
        'fact': 'The chance to run into a person of ' + religion.religion + ' religion in the country ' + country +
                ' is above ' + str(fact_percentage) + '%',
        'hint': 'The religion ' + religion.religion + ' is the ' + str(religion_position + 1)
                + 'th common religion in the country ' + country,
        'answer': real_or_fake,
        'details': 'The estimated percentage of people practising the religion ' + religion.religion +
                ' in the country ' + country + ' is ' + str(religion.percentage) + '%',
    }

# is_common
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming certain religion is common in the given country
# the player should determine whether it is true or false
def is_common_religion(country: str, real_or_fake:bool):
    # get country religions
    religions_data = ReligionsData()
    religions = religions_data.get_country_religions(country)
    if religions is None or len(religions) < 2:
        return None
    if country == 'Germany':
        return None

    # select randomly specific religion
    selected_religion_idx = randint(1, len(religions) - 1)
    selected_religion = religions[selected_religion_idx]
    if religions_data.is_invalid_religion(selected_religion.religion):
        return None

    # other religions for the hint
    del religions[selected_religion_idx]
    other_religions = ''
    for religion in religions:
        other_religions += religion.religion + ', '
    other_religions = other_religions[:-2]

    return {
        'topic': 'Religion', 
        'fact': 'The religion ' + selected_religion.religion + ' is common in ' + country +
         '. (common means there is non-zero proportion of the population which pursue this religion in the country)',
        'hint': 'The religions that are common in the country ' + country + ' is ' + other_religions,
        'answer': True,
        'details': 'The estimated percentage of religion ' + selected_religion.religion + ' in the country ' + country +
                   ' is ' + str(selected_religion.percentage),
    }

# compare_common_religion
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming the proportion of certain religion is more common in the first
# country then the second country - the player should determine whether it is true or false
def compare_common_religion(first: str, second: str):
    # get common religions of the given countries
    religion_data = ReligionsData()
    common_religions = religion_data.common_religions(first, second)
    if common_religions is None or len(common_religions) == 0:
        return None
    selected_religion = common_religions[randint(0, len(common_religions) - 1)]
    if religion_data.is_invalid_religion(selected_religion['first'].religion) or \
            religion_data.is_invalid_religion(selected_religion['second'].religion):
        return None
    if first == 'Germany' or second == 'Germany':
        return None

    return {
        'topic': 'Society',
        'fact': 'The proportion of religion ' + selected_religion['first'].religion + ' in the country ' + first +
                ' is larger then its proportion in the country ' + second,
        'hint': 'The proportion of the religion ' + selected_religion['first'].religion + ' in the country ' + first +
            ' is ' + str(selected_religion['first'].percentage),
        'answer': selected_religion['first'].percentage > selected_religion['second'].percentage,
        'detail': 'The proportion of the religion ' + selected_religion['first'].religion + ' in the country ' + first +
                ' is ' + str(selected_religion['first'].percentage) + ' whereas its proportion in the country ' + second +
                ' is ' + str(selected_religion['second'].percentage),
    }

# compare_main_groups
# the method receives name of two countries and
# construct a fact claiming the main group in first country is more common then the main group in second country
# the player should determine whether it is true or false
def compare_main_religions(first: str, second: str):
    religion_data = ReligionsData()
    first_main_religion = religion_data.main_religion(country=first)
    second_main_religion = religion_data.main_religion(country=second)
    if first_main_religion is None or second_main_religion is None or \
            religion_data.is_invalid_religion(first_main_religion.religion) or religion_data.is_invalid_religion(second_main_religion.religion):
        return None
    if first == 'Germany' or second == 'Germany':
        return None
    answer = first_main_religion.percentage > second_main_religion.percentage
    return {
        'topic': 'Society',
        'fact': 'The main religion in the country ' + first + ' (' + first_main_religion.religion +
            ') has a bigger proportion then the most common religion in the country ' + second + ' (' + second_main_religion.religion + ')',
        'hint': 'The proportion of the religion ' + first_main_religion.religion + ' in the country ' + first +
                ' is ' + str(first_main_religion.percentage),
        'answer': answer,
        'detail': 'The proportion of the religion ' + first_main_religion.religion + ' in the country ' + first +
                ' is ' + str(first_main_religion.percentage) + ' whereas the proportion of the religion ' + second_main_religion.religion +
                ' in the country ' + second + ' is ' + str(second_main_religion.percentage)
    }