from db.business_logic.countries import CountriesData
from db.business_logic.languages import LanguageData
from db.business_logic.ethnics import EthnicsData
from facts.general import compare_field, rank_field, rank_field_continent
from random import randint

############## facts: languages ##########################

# is_same_language
# the method receives name of two countries and
# construct a fact claims that the countries has the same official language
# the player should determine whether it is true or false 
def is_same_language(first: str, second: str):
    lang_data = LanguageData()
    first_language = lang_data.official_language(first)
    second_language = lang_data.official_language(second)
    answer = first_language.language == second_language.language
    return {
        'topic': 'Society', 
        'fact': 'The countries ' + first + ', ' + second + ' has the same official language',
        'hint': 'The official language of country ' + first + ' is ' + first_language.language,
        'answer': answer,
        'detail': 'Both countries ' + first + ', ' + second + ' has the same official language ' + first_language.language if answer else 
            'The official language of the country ' + first + ' is ' + first_language.language
            + ' whereas, the official language of the country ' + second + ' is ' + second_language.language
    }

def more_common_language(country: str, real_or_fake: bool):
    lang_data = LanguageData()
    languages = lang_data.country_languages(country)
    second_language = randint(1, len(languages) - 1)
    first_language = randint(0, second_language - 1)
    if not real_or_fake:
        first_language, second_language = second_language, first_language
    return {
        'topic': 'Society', 
        'fact': 'The language ' + languages[first_language].language + ' is more common then ' + languages[second_language].language + ' in the country ' + country,
        'hint': 'The estimated percentage of language ' + languages[second_language].language + ' in the country ' + country + ' is ' + str(languages[second_language].percentage),
        'answer': real_or_fake,
        'details': 'The estimated percentage of language ' + languages[first_language].language + ' in the country ' + country + ' is ' + str(languages[first_language].percentage) + 
                   ' whereas the estimated percentage of religion ' + languages[second_language].language +
                   ' in the country ' + country + ' is ' + str(languages[second_language].percentage),
    }

def is_common(country: str, real_or_fake: str):
    lang_data = LanguageData()
    languages = lang_data.country_languages(country)
    language = languages[randint(0, len(languages) - 1)]
    return {
        'topic': 'Society', 
        'fact': 'The religion ' + language.language + ' is common in ' + country + ' (common means there is non-zero percentage of people that pursue this religion in the country)',
        'hint': '',
        'answer': real_or_fake,
        'details': 'The estimated percentage of religion ' + language.language + ' in the country ' + country + ' is ' + str(language.percentage),
    }

def above_percentage(country: str, real_or_fake: bool):
    lang_data = LanguageData()
    languages = lang_data.country_languages(country)
    language = languages[randint(0, len(languages) - 1)]
    
    fact_percentage = int(language.percentage)
    if fact_percentage > 9:
        fact_percentage = fact_percentage - (fact_percentage % 10)
        if not real_or_fake:
            fact_percentage += 10
    else:
        fact_percentage = 10 if fact_percentage >= 5 else 5
    return {
        'topic': 'Society', 
        'fact': 'The chance to run into a person speaks in the language ' + language.language + ' is above ' + str(fact_percentage) + '%',
        'hint': '',
        'answer': real_or_fake,
        'details': 'The estimated percentage of people speaking in language ' + language.language + ' in the country ' + country + ' is ' + str(language.percentage) + '%',
    }

############## facts: ethnic groups ##########################

# compare_main_groups
# the method receives name of two countries and
# construct a fact claiming the main group in first country is more common then the main group in second country
# the player should determine whether it is true or false
def compare_main_groups(first: str, second: str):
    # get countries main ethnic group
    ethnic_data = EthnicsData()
    first_group = ethnic_data.main_ethnic_group(country=first)
    second_group = ethnic_data.main_ethnic_group(country=second)
    if first_group is None or second_group is None:
        return None
    answer = first_group.percentage > second_group.percentage
    return {
        'topic': 'Society',
        'fact': 'The main ethnic group in the country ' + first + ' (' + first_group.name +
            ') has a bigger proportion then the most common ethnic group in the country ' + second + ' (' + second_group.name + ')',
        'hint': 'The proportion of the ethnic group ' + first_group.name + ' in the country ' + first +
                ' is ' + str(first_group.percentage),
        'answer': answer,
        'detail': 'The proportion of the ethnic group ' + first_group.name + ' in the country ' + first +
                ' is ' + str(first_group.percentage) + ' whereas the proportion of the ethnic group ' + second_group.name +
                ' in the country ' + second + ' is ' + str(second_group.percentage)
    }

# compare_ethnics_proportion
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming certain random religion is more common then another religion in country X
# the player should determine whether it is true or false
def compare_ethnics_proportion(country: str, real_or_fake: bool):
    ethnic_data = EthnicsData()
    ethnic_groups = ethnic_data.country_ethnic_groups(country=country)
    if ethnic_groups is None or len(ethnic_groups) < 3:
        return None

    second_group = randint(2, len(ethnic_groups) - 1)
    first_group = randint(1, second_group - 1)
    if not real_or_fake:
        first_group, second_group = second_group, first_group
    return {
        'topic': 'Society',
        'fact': 'The ethnic group ' + ethnic_groups[first_group].name + ' is more common then ' +
                ethnic_groups[second_group].name + ' in the country ' + country,
        'hint': 'The estimated proportion of the ethnic group ' + ethnic_groups[second_group].name
                + ' in the country ' + country + ' is ' + str(ethnic_groups[second_group].percentage),
        'answer': real_or_fake,
        'detail': 'The estimated proportion of the ethnic group ' + ethnic_groups[first_group].name +
            ' in the country ' + country + ' is ' + str(ethnic_groups[first_group].percentage) +
            ' whereas the approximated proportion of the ethnic group ' + ethnic_groups[second_group].name +
            ' in the country ' + country + ' is ' + str(ethnic_groups[second_group].percentage),
    }

# ethnic_above_percentage
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming the proportion of certain ethnic group is above X% in the given country.
# the player should determine whether it is true or false
def ethnic_above_percentage(country: str, real_or_fake: bool):
    # get ethnic groups of the given country
    ethnic_data = EthnicsData()
    ethnics_groups = ethnic_data.country_ethnic_groups(country=country)
    if ethnics_groups is None or len(ethnics_groups) == 0:
        return None

    # select specific ethnic group
    selected_group_idx = randint(0, len(ethnics_groups) - 1)
    selected_group = ethnics_groups[selected_group_idx]

    # compute the proportion appeared in the statement
    statement_percentage = int(selected_group.percentage)
    if statement_percentage > 9:
        statement_percentage = statement_percentage - (statement_percentage % 10)
        if not real_or_fake:
            statement_percentage += 10
    else:
        statement_percentage = 10 if statement_percentage >= 5 else 5
    return {
        'topic': 'Society',
        'fact': 'The chance to run into a person of the ethnic group ' + selected_group.name +
                ' in the country ' + country + ' is above ' + str(statement_percentage) + '%',
        'hint': 'The ethnic group ' + selected_group.name + ' is the ' + str(selected_group_idx + 1) +
                'th with the largest proportion of the population in the country ' + country,
        'answer': real_or_fake,
        'detail': 'The estimated proportion of the ethnic group ' + selected_group.name +
                ' in the country ' + country + ' is ' + str(selected_group.percentage) + '%',
    }

# compare_common_ethnic
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming the proportion of certain common ethnic group is more common in first
# country then the second country - the player should determine whether it is true or false
def compare_common_ethnic(first: str, second: str):
    # get common ethnic groups of the given countries
    ethnic_data = EthnicsData()
    ethnics_groups = ethnic_data.common_ethnics(first, second)
    if ethnics_groups is None or len(ethnics_groups) == 0:
        return None
    selected_groups = ethnics_groups[randint(0, len(ethnics_groups) - 1)]
    return {
        'topic': 'Society',
        'fact': 'The proportion of ethnic group ' + selected_groups['first'].name + ' in the country ' + first +
                ' is larger then its proportion in the country ' + second,
        'hint': 'The proportion of the ethnic group '+ selected_groups['first'].name + ' in the country ' + first +
            ' is ' + str(selected_groups['first'].percentage),
        'answer': selected_groups['first'].percentage > selected_groups['second'].percentage,
        'detail': 'The proportion of the ethnic group ' + selected_groups['first'].name + ' in the country ' + first +
                ' is ' + str(selected_groups['first'].percentage) + ' whereas its proportion in the country ' + second +
                ' is ' + str(selected_groups['second'].percentage),
    }


############## facts: compare countries fields ##########################

# compare_unemployment_rate
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total revenues.
def compare_unemployment_rate(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='unemployment_rate', field_display='unemployment rate')

# compare_area
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of area size.
def compare_area(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='area', field_display='area size')

# compare_population
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of population size.
def compare_population(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='population', field_display='population')

# compare_internet_users
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of internet users.
def compare_internet_users(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='internet_users', field_display='internet users')

# compare_internet_users
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of internet users.
def compare_cellular_subscriptions(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='cellular_subscriptions', field_display='cellular subscriptions')

# compare_life_expectancy
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the average life expectancy.
def compare_life_expectancy(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='total_expectancy', field_display='average life expectancy')

def compare_male_expectancy(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='male_expectancy', field_display='average male\'s life expectancy')

def compare_female_expectancy(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='female_expectancy', field_display='average female\'s life expectancy')

# compare_median_age, compare_male_median_age, compare_female_median_age
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of median age.
def compare_median_age(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='total_median_age', field_display='median age')

def compare_male_median_age(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='male_median_age', field_display='male\'s median age',)

def compare_female_median_age(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='female_median_age', field_display='female\'s median age',)

# compare_birth_rate, compare_death_rate
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of birth/death rate.
def compare_birth_rate(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='birth_rate', field_display='birth rate')

def compare_death_rate(first: str, second: str):
    return compare_field(topic='Society', first=first, second=second, field='death_rate', field_display='death rate')


############## facts: compare fields ####################

# compare_birth_death_rate
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming that the birth rate of given country is smaller/larger to its death rate
# the player should determine whether it is true or false
def compare_birth_death_rate(country: str, real_or_fake: bool):
    # get the country data
    countries_data = CountriesData()
    country = countries_data.country_data(country=country)
    if (real_or_fake and country.birth_rate > country.death_rate) or (not real_or_fake and country.birth_rate < country.death_rate):
        comparison = 'larger'
    else:
        comparison = 'smaller'

    return {
        'topic': 'Society',
        'fact': 'The birth rate in the country ' + country.name + ' is ' + comparison + ' then the country\'s death rate',
        'hint': 'The birth rate in the country ' + country.name + ' is ' + str(country.birth_rate),
        'answer': real_or_fake,
        'detail': 'The birth rate in the country ' + country.name + ' is ' + str(country.birth_rate) +
                ' whereas the death rate is ' + str(country.death_rate),
    }

# compare_male_female_expectancy
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming that the male life expectancy of given country is smaller/larger to the female's life expectancy
# the player should determine whether it is true or false
def compare_male_female_expectancy(country: str, real_or_fake: bool):
    # get the country data
    countries_data = CountriesData()
    country = countries_data.country_data(country=country)
    if (real_or_fake and country.male_expectancy > country.female_expectancy) or (not real_or_fake and country.male_expectancy < country.female_expectancy):
        comparison = 'larger'
    else:
        comparison = 'smaller'

    return {
        'topic': 'Society',
        'fact': 'Male\'s life expectancy in the country ' + country.name + ' is '
                + comparison + ' then the female\'s life expectancy in the country',
        'hint': 'Male\'s life expectancy in the country ' + country.name + ' is ' + str(country.male_expectancy),
        'answer': real_or_fake,
        'detail': 'The male\'s life expectancy in the country ' + country.name + ' is ' + str(country.male_expectancy) +
                ' whereas the female\'s life expectancy is ' + str(country.female_expectancy),
    }

# compare_male_female_median
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact claiming that the male median age of given country is smaller/larger to the female's median age
# the player should determine whether it is true or false
def compare_male_female_median(country: str, real_or_fake: bool):
    # get the country data
    countries_data = CountriesData()
    country = countries_data.country_data(country=country)
    if (real_or_fake and country.male_median_age > country.female_median_age) or (not real_or_fake and country.male_median_age < country.female_median_age):
        comparison = 'larger'
    else:
        comparison = 'smaller'

    return {
        'topic': 'Society',
        'fact': 'Male\'s median age in the country ' + country.name + ' is '
                + comparison + ' then the female\'s life expectancy in the country',
        'hint': 'Male\'s median age in the country ' + country.name + ' is ' + str(country.male_median_age),
        'answer': real_or_fake,
        'detail': 'The male\'s median age in the country ' + country.name + ' is ' + str(country.male_median_age) +
                ' whereas the female\'s median age is ' + str(country.female_median_age),
    }

# age_range_compare
# the method receives name of a country, and boolean variable indicate whether to build a true fact or a fake one
# and construct a fact comparing the proportion in the population of two age ranges.
def age_range_compare(country: str, real_or_fake: bool):
    # get the country data
    countries_data = CountriesData()
    country = countries_data.country_data(country=country)

    # select age ranges to compare
    age_ranges = ['_0_14_years', '_15_24_years', '_25_54_years', '_55_64_years', '_65_over']
    display_age_ranges = ['0-14 years', '15-24 years', '25-54 years', '55-64 years', 'over 65']
    first_compare = randint(0, len(age_ranges) - 1)
    first_value = getattr(country, age_ranges[first_compare])
    second_compare = randint(0, len(age_ranges) - 1)
    second_value = getattr(country, age_ranges[second_compare])
    if first_value == second_value:
        second_compare = (first_compare + 1) % len(age_ranges)

    # construct a real or fake fact according to the given arguments
    if (real_or_fake and first_value > second_value) or (not real_or_fake and first_value < second_value):
        comparison = 'larger'
    else:
        comparison = 'smaller'

    # returns the fact content
    return {
        'topic': 'Society',
        'fact': 'The country ' + country.name + ' population is divided into the following age ranges: 0-14 years, 15-24 years, 25-54 years, 55-64 years, over 65. ' +
            ' The proportion of age group ' + display_age_ranges[first_compare] + ' is ' + comparison + ' then the range ' + display_age_ranges[second_compare],
        'hint': 'The proportion of age group ' + display_age_ranges[first_compare] + ' of the entire population is ' + str(first_value),
        'answer': real_or_fake,
        'detail': 'The proportion of age group ' + display_age_ranges[first_compare] + ' of the entire population is ' + str(first_value) +
            ' whereas the proportion of age group ' + display_age_ranges[second_compare] + ' is ' + str(second_value)
    }



############## facts: ranks ##########################

# ranks among the countries in the entire world
def rank_population(country: str, real_or_fake:bool):
    return rank_field(topic='Society', country=country, field='population', field_display='population size', real_or_fake=real_or_fake)

def rank_unemployment_rate(country: str, real_or_fake: bool):
    return rank_field(topic='Society', country=country, field='unemployment_rate', field_display='unemployment rate', real_or_fake=real_or_fake)

def rank_median_age(country: str, real_or_fake:bool):
    return rank_field(topic='Society', country=country, field='total_median_age', field_display='median age', real_or_fake=real_or_fake)

def rank_expectancy_age(country: str, real_or_fake: bool):
    return rank_field(topic='Society', country=country, field='total_expectancy', field_display='life expectancy', real_or_fake=real_or_fake)

def rank_birth_rate(country: str, real_or_fake:bool):
    return rank_field(topic='Society', country=country, field='birth_rate', field_display='birth rate', real_or_fake=real_or_fake)

def rank_death_rate(country: str, real_or_fake:bool):
    return rank_field(topic='Society', country=country, field='death_rate', field_display='death rate', real_or_fake=real_or_fake)

def rank_internet_users(country: str, real_or_fake:bool):
    return rank_field(topic='Society', country=country, field='internet_users', field_display='internet users', real_or_fake=real_or_fake)

# ranks among the countries in the same continent
def rank_population_continent(country: str, real_or_fake:bool):
    return rank_field_continent(topic='Society', country=country, field='population', field_display='population size', real_or_fake=real_or_fake)

def rank_unemployment_rate_continent(country: str, real_or_fake: bool):
    return rank_field_continent(topic='Society', country=country, field='unemployment_rate', field_display='unemployment rate', real_or_fake=real_or_fake)

def rank_expectancy_age_continent(country: str, real_or_fake: bool):
    return rank_field_continent(topic='Society', country=country, field='total_expectancy', field_display='life expectancy', real_or_fake=real_or_fake)
