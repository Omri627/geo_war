from db.business_logic.countries import CountriesData
from db.business_logic.cities import CitiesData
from random import randint, choice
from db.business_logic.utils import rank_top_fact

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
        'fact': 'the number of towns in the country ' + first + ' is larger then in the country ' + second,
        'hint': 'the difference between the number of towns in this two countries is: ' + str(abs(first_quantity - second_quantity)),
        'answer': first_quantity > second_quantity,
        'detail': 'the number of towns in the country ' + first + ' is ' + str(first_quantity) +
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
        hint = 'the number of towns in the country ' + country + ' is significantly more or less then ' + str(cmp_quantity)
    else:
        hint = 'the number of towns in the country ' + country + ' is relatively close to ' + str(cmp_quantity)
    return {
        'topic': 'Geography', 
        'fact': 'the number of towns in the country ' + country + " is larger then " + str(cmp_quantity),
        'hint': hint,
        'answer': quantity > cmp_quantity,
        'detail': 'the number of towns in the country ' + country + ' is ' + str(quantity)
    }

############## facts: capital city ##########################

# is_capital
# the method receives name of country, and boolean variable indicate whether to build a true fact of fake
# and construct a fact that display random big city on the screen and claims it is the capital city of the country
# the player should determine whether it is true or false
def is_capital(country: str, real_or_fake: bool):
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
        detail = 'The most populated city in the country ' + country + ' is ' + most_populated.name + ' placed in the position ' \
                 + str(position) + ' in population size of the entire world'
    return {
        'topic': 'Geography', 
        'fact': fact,
        'hint': 'The population size of the city ' + most_populated.name + ' is ' + str(most_populated.population),
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

