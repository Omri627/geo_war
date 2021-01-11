from db.business_logic.countries import CountriesData
from db.business_logic.cities import CitiesData
from random import randint, choice
from db.business_logic.utils import rank_top_fact, float_display
from facts.general import compare_field, rank_field, rank_field_continent

############## facts: quantity of cities ##########################

# compare_cities_quantity
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries cities quantity.
def compare_cities_quantity(first: str, second: str):
    cities_data = CitiesData()
    first_quantity = cities_data.cities_quantity(first)
    second_quantity = cities_data.cities_quantity(second)
    return {
        'topic': 'Geography', 
        'fact': 'The number of towns in the country ' + first + ' is larger then in the country ' + second,
        'hint': 'The difference between the number of towns in this two countries is: ' + str(abs(first_quantity - second_quantity)),
        'answer': first_quantity > second_quantity,
        'detail': 'The number of towns in the country ' + first + ' is ' + str(first_quantity) +
                  ' whilst the amount of towns in the country ' + second + ' is ' + str(second_quantity)
    }

# has_more_then
# the method receives a country and
# construct a fact compare the number of cities of the given country to a value close to it
def has_more_cities_then(country: str, real_or_fake: bool):
    cities_data = CitiesData()
    quantity = cities_data.cities_quantity(country)
    options = [50, 100, 500, 1000, 5000, 100000, 50000, 100000, 500000, 1000000]
    index = len(options)
    for i in range(0, len(options)):
        if options[i] > quantity:
            index = i
            break
    index = min(index + 2, len(options))

    cmp_quantity = options[randint(0, index)]
    if abs(quantity - cmp_quantity) > 500:
        hint = 'The number of towns in the country ' + country + ' is significantly more or less then ' + str(cmp_quantity)
    else:
        hint = 'The number of towns in the country ' + country + ' is relatively close to ' + str(cmp_quantity)
    return {
        'topic': 'Geography', 
        'fact': 'The number of towns in the country ' + country + " is larger then " + str(cmp_quantity),
        'hint': hint,
        'answer': quantity > cmp_quantity,
        'detail': 'The number of towns in the country ' + country + ' is ' + str(quantity)
    }

############## facts: area ###############################
def rank_area(country: str, real_or_fake: bool):
    return rank_field(topic='Geography', country=country, field='area', field_display='area size', real_or_fake=real_or_fake)

def rank_area_continent(country: str, real_or_fake: bool):
    return rank_field_continent(topic='Geography', country=country, field='area', field_display='area size', real_or_fake=real_or_fake)

def compare_population_density(first: str, second: str):
    countries_data = CountriesData()
    first_pd = countries_data.country_population_density(country=first)
    second_pd = countries_data.country_population_density(country=second)
    if first_pd is None or second_pd is None or first_pd == -1 or second_pd == -1:
        return None
    return {
        'topic': 'Geography',
        'fact': 'the country ' + first + ' has a larger population density then ' + second,
        'hint': 'The difference of their population density is ' + float_display(abs(first_pd - second_pd)),
        'answer': first_pd > second_pd,
        'detail': 'the country ' + first + ' has population size of ' + str(first_pd) +
                  ' whereas the country ' + second + ' has population size of ' + str(second_pd),
    }

def evaluate_population(country: str, real_or_fake: str):
    countries_data = CountriesData()
    country = countries_data.country_data(country=country)
    populations = [5000000, 7500000, 10000000, 50000000, 75000000, 100000000, 250000000, 500000000]
    fact_population = choice(populations)

    # hint: significant difference or not
    if abs(country.population - fact_population) > 5000000:
        hint = 'The population size of the country ' + country.name + ' is significantly more or less then ' + str(fact_population)
    else:
        hint = 'The population size of the country ' + country.name + ' is relatively close to ' + str(fact_population)
    return {
        'topic': 'Geography',
        'fact': 'the country ' + country.name + ' has a larger population size then ' + str(fact_population),
        'hint': hint,
        'answer': country.population > fact_population,
        'detail': 'the country ' + country.name + ' has population size of ' + str(country.population)
    }

def rank_population_density(country: str, real_or_fake: bool):
    countries_data = CountriesData()
    position = countries_data.rank_population_density(country)
    country_object = countries_data.country_data(country)
    population_density = country_object.population / country_object.area
    if position < 3:
        return None

    top_position = rank_top_fact(position, real_or_fake)
    fact = 'The country ' + country + ' is in the top ' + str(top_position) + ' in population density in the entire world'
    detail = 'The country ' + country + ' is ranked ' + str(position) + ' in population density of the entire world'
    return {
        'topic': 'Geography',
        'fact': fact,
        'hint':  'The country ' + country + ' has an population density of ' + str(population_density),
        'answer': real_or_fake,
        'detail': detail
    }


############## facts: capital city ##########################

# is_capital
# the method receives name of country, and boolean variable indicate whether to build a true fact of fake
# and construct a fact that display random big city on the screen and claims it is the capital city of the country
# the player should determine whether it is true or false
def is_capital(country: str, real_or_fake: bool):
    if country == 'United Kingdom' or country == 'United States' or country == 'Italy':
        return None
    cities_data = CitiesData()
    capital = cities_data.capital_city(country=country)
    cities = cities_data.most_populated(country=country, quantity=10)
    if capital is None or cities is None or len(cities) < 3:
        return None

    upper_bound = min(5, len(cities) - 1)
    if real_or_fake:
        random_big_city = capital
    else: 
        random_big_city = cities[randint(1, upper_bound)].name

    # select cities for hints
    hints = [cities[0].name, cities[1].name, cities[2].name]
    if random_big_city not in hints:
        hints.insert(0, random_big_city)

    return {
        'topic': 'Geography', 
        'fact': 'The capital city of the ' + country + ' is ' + random_big_city,
        'hint': 'The capital city of the country is one of the following: ' + hints[0] + ', ' + hints[1] + ', ' + hints[2],
        'answer': random_big_city == capital,
        'detail': 'The capital city of the ' + country + " is " + capital
    }

############## facts: population ##########################

# most_populated
# the method receives name of country, and boolean variable indicate whether to build a true fact of fake
# and construct a fact that display random big city on the screen and claims it is the most populated city in country
# the player should determine whether it is true or false
def most_populated(country: str, real_or_fake: bool):
    if country == 'United Kingdom' or country == 'United States' or country == 'Italy':
        return None
    cities_data = CitiesData()
    cities = cities_data.most_populated(country=country, quantity=10)
    if cities is None or len(cities) < 3:
        return None

    # select a random city
    upper_bound = min(5, len(cities) - 1)
    largest_city = cities[0]
    if real_or_fake:
        selected_index = 0
    else:
        selected_index = randint(1, upper_bound)
    selected_city = cities[selected_index]

    # store viable possibilities for the hint
    hints = [0, 1, 3]
    if selected_index not in hints:
        hints.insert(0, selected_index)

    # return the fact content
    return {
        'topic': 'Geography', 
        'fact': 'The city which contains the largest population in the country ' + country + " is " + selected_city.name,
        'hint': 'The city with the largest population size is one of the following: ' + cities[hints[0]].name
                + ', ' + cities[hints[1]].name + ", " + cities[hints[2]].name,
        'answer': largest_city.name == selected_city.name,
        'detail': 'The city with largest population in the country ' + country + " is " + largest_city.name
    }

# cities_larger_country
# the method receives name of two countries denoted as first and second and
# construct a fact that compare the population size of big cities of first country
# and the population size of the entire country.
def cities_larger_country(first: str, second: str):
    if second == 'United Kingdom' or second == 'United States' or second == 'Italy':
        return None
    # interact with business logic functionality
    cities_data = CitiesData()
    countries_data = CountriesData()

    # receives essential data from the repository
    cities = cities_data.cities_larger_country(first, second)
    first_country = countries_data.country_data(first)
    if cities is None or len(cities) == 0:
        return None
    selected_city = choice(cities)

    return {
        'topic': 'Geography', 
        'fact': 'The city ' + selected_city['name'] + ' itself has a larger population than the entire state of ' + first,
        'hint': 'The population size of the city ' + selected_city['name'] + ' is ' + str(selected_city['population']),
        'answer': selected_city['is_bigger'],
        'detail': 'The population size of the city ' + selected_city['name'] + ' is ' + str(selected_city['population'])
                + ' whereas the population size of the state ' + first + ' is ' + str(first_country.population),
    }

# rank_populated_city
# the method receives name of country, and boolean variable indicate whether to build a true fact of fake
# and construct a fact claiming the most populated city in the given country is in top X in the entire world. 
# the player should determine whether it is true or false
def rank_populated_city(country: str, real_or_fake: bool):
    if country == 'United Kingdom' or country == 'United States' or country == 'Italy':
        return None
    cities_data = CitiesData()
    position = cities_data.position_populated_city(country)
    most_populated = cities_data.most_populated(country=country, quantity=1)
    if most_populated is None or len(most_populated) == 0:
        return None
    most_populated = most_populated[0]
    if position == 1:
        fact = 'The most populated city in the country ' + country + ' ' + most_populated.name + ' is the most populated in the entire world'
        detail = fact + ' with population of ' + str(most_populated.population)
        real_or_fake = True
    else:
        top_position = rank_top_fact(position, real_or_fake)

        fact = 'The most populated city in the country ' + country + ' ' + most_populated.name + \
               ' is in the top ' + str(top_position) + ' cities in population size of the entire world'
        detail = 'The city ' + most_populated.name + ' is ' \
                 + str(position) + 'th most populated city of the entire world'
    return {
        'topic': 'Geography', 
        'fact': fact,
        'hint': 'The population size of the city ' + most_populated.name + ' is ' + str(most_populated.population),
        'answer': real_or_fake,
        'detail': detail
    }

# rank_populated_city_continent
# the method receives name of country, and boolean variable indicate whether to build a true fact of fake
# and construct a fact claiming a random city in the given country is in top X among cities in same continent.
# the player should determine whether it is true or false
def rank_populated_city_continent(country: str, real_or_fake: bool):
    if country == 'United Kingdom' or country == 'United States' or country == 'Italy':
        return None
    cities_data = CitiesData()
    countries_data = CountriesData()
    most_populated = cities_data.most_populated(country=country, quantity=5)
    if most_populated is None or len(most_populated) == 0:
        return None
    selected_city = most_populated[randint(0, min(5, len(most_populated) - 1))]
    position = cities_data.position_populated_city_continent(country, selected_city.name)
    continent = countries_data.country_data(country=country).continent
    if position == 1:
        fact = 'The city ' + selected_city.name + ' is the most populated in ' + continent
        detail = fact + ' with population of ' + str(int(selected_city.population))
        real_or_fake = True
    else:
        options = [20, 50, 100, 200, 500, 1000]
        top_position = choice(options)
        real_or_fake = position < top_position

        fact = 'The city ' + selected_city.name + ' is in top ' + str(top_position) + ' most populated cities in ' + continent
        detail = 'The city ' + selected_city.name + ' is ' + str(position) + 'th most populated cities in ' + continent
    return {
        'topic': 'Geography',
        'fact': fact,
        'hint': 'The population size of the city ' + selected_city.name + ' is ' + str(selected_city.population),
        'answer': real_or_fake,
        'detail': detail
    }

############## facts: other ##########################
# is_same_continent
# the method receives name of two countries and
# construct a fact claims that the countries has the same continent
# the player should determine whether it is true or false 
def is_same_continent(first: str, second: str):
    countries_data = CountriesData()
    first_country = countries_data.country_data(country=first)
    second_country = countries_data.country_data(country=second)
    if first_country is None or second_country is None:
        return None
    real_or_fake = first_country.continent == second_country.continent
    return {
        'topic': 'Geography', 
        'fact': 'The countries ' + first + ' and ' + second + ' located in the same continent',
        'hint': 'The country ' + first + ' located in the continent ' + first_country.continent,
        'answer': real_or_fake,
        'detail': 'Both countries ' + first + ', ' + second + ' located in the continent ' + first_country.continent if real_or_fake else
            'The country ' + first + ' located in continent ' + first_country.continent +
            ' whereas the country ' + second + ' located in continent ' + second_country.continent
    }

def continent_quantity(country: str, real_or_fake: bool):
    countries_data = CountriesData()
    country_object = countries_data.country_data(country=country)
    continent_amount = countries_data.country_continent_quantity(country=country)
    options = [35, 40, 50, 70, 100, 150, 200]
    fact_quantity = choice(options)

    # evaluate hint
    hint = min(continent_amount - (continent_amount % 10) - 10, fact_quantity - 10)
    return {
        'topic': 'Geography',
        'fact': 'The number of countries in ' + country_object.continent + ' is above ' + str(
            fact_quantity) + ' (the continent of the country ' + country + ')',
        'hint': 'The number of countries in ' + country_object.continent + ' is greater then ' + str(hint),
        'answer': continent_amount > fact_quantity,
        'detail': 'The number of countries in ' + country_object.continent + ' is ' + str(continent_amount),
    }
