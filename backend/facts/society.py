from db.business_logic.countries import CountriesData


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
            'The official language of the country ' + first + ' is ' + first_language.language + ' whereas, the official language of the country ' + second + ' is ' + second_language.language
    }

def more_common_language(country: str, real_or_fake: bool):
    lang_data = LanguageData()
    languages = lang_data.country_languages(country)
    second_language = randint(1, len(languages) - 1)
    first_language = randint(0, second_language - 1)
    if not real_or_fake:
        first_religion, second_religion = second_religion, first_religion
    return {
        'topic': 'Society', 
        'fact': 'The language ' + languages[first_language].language + ' is more common then ' + languages[second_language].language + ' in the country ' + country,
        'hint': 'The estimated percentage of language ' + languages[second_language].language + ' in the country ' + country + ' is ' + str(languages[second_language].percentage),
        'answer': real_or_fake,
        'details': 'The estimated percentage of language ' + languages[first_language].language + ' in the country ' + country + ' is ' + str(languages[first_language].percentage) + 
                   ' whereas the estimated percentage of religion ' + languages[second_language].language + ' in the country ' + country + ' is ' + str(languages[second_language].percentage),
    }

def is_common(country: str, real_or_fake: str):
    lang_data = LanguageData()
    languages = lang_data.country_languages(country)
    language = languages[randint(0, len(languages) - 1)]
    return {
        'topic': 'Society', 
        'fact': 'The religion ' + language.language + ' is common in ' +  country. + ' (common means there is non-zero percentage of people that pursue this religion in the country)',
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


############## facts: compare countries fields ##########################

# compare_field
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of given field.
def compare_field(first: str, second: str, field: str):
    countries_data = CountriesData()
    first_country = countries_data.country_data(country=first)
    second_country = countries_data.country_data(country=second)
    first_field = getattr(first_country, field)
    second_field = getattr(second_country, field)
    return {
        'topic': 'Economy', 
        'fact': 'the country ' + first + ' has a higher ' + field + ' then ' + second,
        'hint': 'The difference of their ' + field + ' is ' + str(abs(first_field - second_field)),
        'answer': first_field > second_field,
        'detail': 'the country ' + first + ' has an ' + field + ' of ' + str(first_field) + " whereas the country " + second + " has an " + field + " of " + str(second_field),
    }

# compare_unemployment_rate
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total revenues.
def compare_unemployment_rate(first: str, second: str):
    return compare_field(first, second, 'unemployment rate')

# compare_area
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of area size.
def compare_area(first: str, second: str):
    return compare_field(first, second, 'area size')

# compare_population
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of population size.
def compare_population(first: str, second: str):
    return compare_field(first, second, 'population')

# compare_life_expetency
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the average life expetency.
def compare_life_expetency(first: str, second: str):
    return compare_field(first, second, 'life expetency')

def compare_male_expetency(first: str, second: str):
    return compare_field(first, second, 'male\'s life expetency', MALE_EXPETENCY)

def compare_female_expetency(first: str, second: str):
    return compare_field(first, second, 'female\'s life expetency')

# compare_median_age, compare_male_median_age, compare_female_median_age
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of median age.
def compare_median_age(first: str, second: str):
    return compare_field(first, second, 'median age')

def compare_male_median_age(first: str, second: str):
    return compare_field(first, second, 'male\'s median age')
.
def compare_female_median_age(first: str, second: str):
    return compare_field(first, second, 'female\'s median age')

# compare_birth_rate, compare_death_rate
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of birth/death rate.
def compare_birth_rate(first: str, second: str):
    return compare_field(first, second, 'birth rate')

def compare_death_rate(first: str, second: str):
    return compare_field(first, second, 'death rate')

