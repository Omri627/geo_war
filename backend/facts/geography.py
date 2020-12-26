from db.business_logic.countries import CountriesData
from db.business_logic.cities import CitiesData
from random import seed
from random import randint

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
        'fact': 'the number of cities in the countries ' + first + ' is larger then in the country ' + second,
        'hint': 'the differnce between the number of cities in this two countries is: ' + str(abs(first_quantity - second_quantity)),
        'answer': first_quantity > second_quantity,
        'detail': 'the number of cities in the country ' + first + ' is ' + str(first_quantity) + ' whlist the amount of cities in the country ' + second + ' is ' + str(second_quantity) 
    }

# has_more_then
# the method receives a country and
# construct a fact compare the number of cities of the given country to a value close to it
def has_more_then(country: str, cmp_quantity: int):
    cities_data = CitiesData()
    quantity = cities_data.cities_quantity(country)
    if abs(quantity - cmp_quantity) > 100:
        hint = 'the number of cities in the country ' + country + ' is sagnificantly more or less then ' + str(cmp_quantity)
    else:
        hint = 'the number of cities in the country ' + country + ' is relatively close to ' + str(cmp_quantity)
    return {
        'topic': 'Geography', 
        'fact': 'the number of cities in the country ' + country + " is larger then " + str(cmp_quantity),
        'hint': hint,
        'answer': quantity > cmp_quantity,
        'detail': 'the number of cities in the country ' + country + ' is ' + str(quantity)
    }

############## facts: capital city ##########################

# is_capital
# the method receives name of country, and boolean variable indicate whether to build a true fact of fake
# and construct a fact that display random big city on the screen and claims it is the capital city of the country
# the player should determine whether it is true or false
def is_capital(country: str, real_or_fake: bool):
    cities_data = CitiesData()
    capital = cities_data.capital_city(country=country)
    if real_or_fake:
        big_city = capital
    else: 
        print (country)
        big_city = cities_data.random_big_city(country=country)
    return {
        'topic': 'Geography', 
        'fact': 'the capital city of the ' + country + " is " + big_city,
        'hint': '',
        'answer': big_city == capital,
        'detail': 'the capital city of the ' + country + " is " + capital
    }

############## facts: population ##########################

# most_populated
# the method receives name of country, and boolean variable indicate whether to build a true fact of fake
# and construct a fact that display random big city on the screen and claims it is the most populated city in country
# the player should determine whether it is true or false
def most_populated(country: str, real_or_fake: bool):
    cities_data = CitiesData()
    cities = cities_data.most_populated(country, 10)
    biggest_city = cities[0][0]
    if real_or_fake:
        selected_city = cities[0][0]
    else:
        selected_city = cities[randint(1, 10)][0]
    return {
        'topic': 'Geography', 
        'fact': 'The city with largest population in the country ' + country + " is " + selected_city,
        'hint': '',
        'answer': biggest_city == selected_city,
        'detail': 'The city with largest population in the country ' + country + " is " + biggest_city
    }

# cities_larger_country
# the method receives name of two countries denoted as first and second and
# construct a fact that compare the population size of big cities of first country and the population size of the entire country.
def cities_larger_country(first: str, second: str):
    cities_data = CitiesData()
    cities = cities_data.cities_larger_country(first, second)
    second_country = cities_data.country_data(second)
    if cities == None or len(cities) == 0:
        return None
    selected_city = cities[randint(0, len(cities))]
    return {
        'topic': 'Geography', 
        'fact': 'The city ' + selected_city[0] + ' itself has a larger population than the entire state of ' + second,
        'hint': 'The population size of the city ' + selected_city[0] + ' is ' + selected_city[1],
        'answer': selected_city[2],
        'detail': 'The population size of the city ' + selected_city[0] + ' is ' + selected_city[1] + ' whereas the population size of the state ' + second + ' is ' + str(second_country.population), 
    }



############## facts: ranks ##########################

# rank_field
# the method receives a name of country, boolean variable indicate whether to build a true fact of fake and a field name
# and construct a fact claiming the country is ranked in top X in the entire world in terms of this field. 
# the player should determine whether it is true or false
def rank_field(country: str, field: str):
    cities_data = CitiesData()
    position = cities_data.rank_field(country, field)
    country_object = cities_data.country_data(country)
    if position == 1:
        fact = 'The country that has the highest ' + field + ' in the world is ' + country
        detail = fact + ' with value of ' + getattr(country_object, field)
    else:
        if real_or_fake:
            top_position = position - (position % 10) + 10
        else:
            top_position = position - (position % 10)
        fact = 'The country ' + country + ' is in the top ' + str(top_position) + ' in ' + field + ' of the entire world'
        detail = 'The country ' + country + ' is ranked ' + str(position) + ' in ' + field + ' of the entire world'
    return {
        'topic': 'Geography', 
        'fact': fact,
        'hint':  'the country ' + first + ' has an ' + field + ' of ' + str(getattr(country_object, field)),
        'answer': real_or_fake,
        'detail': detail
    }

# rank_populated_city
# the method receives name of country, and boolean variable indicate whether to build a true fact of fake
# and construct a fact claiming the most populated city in the given country is in top X in the entire world. 
# the player should determine whether it is true or false
def rank_populated_city(country: str, real_or_fake: bool):
    cities_data = CitiesData()
    position = cities_data.position_populated_city(country, 10)
    most_populated = cities_data.most_populated(country)
    if position == 1:
        fact = 'The most populated city in the country ' + country + ' is the most populated in the entire world'
        detail = fact + ' with population of ' + most_populated[1]
    else:
        if real_or_fake:
            top_position = position - (position % 10) + 10
        else:
            top_position = position - (position % 10)
        fact = 'The most populated city in the country ' + country + ' is in the top ' + str(top_position) + ' in population size of the entire world'
        detail = 'The most populated city in the country ' + country + ' is in the position ' + str(position) + ' in population size of the entire world'
    return {
        'topic': 'Geography', 
        'fact': fact,
        'hint': 'The most populated city in the country ' + country + ' is ' + most_populated,
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
    answer = first_country.continent == second_country.continent
    return {
        'topic': 'Geography', 
        'fact': 'The countries ' + first + ', ' + second + ' located in the same continent',
        'hint': '',
        'answer': answer,
        'detail': 'Both countries ' + first + ', ' + second + ' located in the continent ' + first_country[0][CONTINENT_COLUMN] if answer else 
            'The country ' + first + ' located in continent ' + first_country[0][CONTINENT_COLUMN] + ' whereas the country ' + second + ' located in continent ' + second_country[0][CONTINENT_COLUMN]
    }

