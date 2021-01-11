from db.business_logic.utils import rank_top_fact, float_display
from db.business_logic.countries import CountriesData

# rank_field
# the method receives a name of country, boolean variable indicate whether to build a true fact of fake and a field name
# and construct a fact claiming the country is ranked in top X in the entire world in terms of this field.
# the player should determine whether it is true or false
def rank_field(topic: str, country: str, field: str, field_display: str, real_or_fake: bool):
    countries_data = CountriesData()
    position = countries_data.rank_field(country, field)
    country_object = countries_data.country_data(country)
    if getattr(country_object, field) is None or getattr(country_object, field) == -1:
        return None
    if position == 1 or (not real_or_fake and position < 4):
        best_country = countries_data.most_field(field, 1)[0]
        fact = 'The country that has the highest ' + field_display + ' in the world is ' + country
        detail = 'The country that has the highest ' + field_display + ' in the world is ' + best_country['name'] + \
                 ' with value of ' + str(best_country['field_value'])
        real_or_fake = position == 1
    else:
        top_position = rank_top_fact(position, real_or_fake)

        fact = 'The country ' + country + ' is in the top ' + str(top_position) + ' in terms of ' + field_display + ' in the entire world'
        detail = 'The country ' + country + ' is ranked ' + str(position) + ' in ' + field_display + ' of the entire world'
    return {
        'topic': topic,
        'fact': fact,
        'hint':  'The country ' + country + ' has an ' + field_display + ' of ' + str(getattr(country_object, field)),
        'answer': real_or_fake,
        'detail': detail
    }

# rank_field
# the method receives a name of country, boolean variable indicate whether to build a true fact of fake and a field name
# and construct a fact claiming the country is ranked in top X in the entire world in terms of this field.
# the player should determine whether it is true or false
def rank_field_continent(topic: str, country: str, field: str, field_display: str, real_or_fake: bool):
    countries_data = CountriesData()
    position = countries_data.rank_field_continent(country, field)
    country_object = countries_data.country_data(country)
    if getattr(country_object, field) is None or getattr(country_object, field) == -1:
        return None
    if position == 1 or (not real_or_fake and position < 4):
        best_country = countries_data.most_field_continent(country_object.continent, field, 1)[0]
        fact = 'The country that has the highest ' + field_display + ' in ' + country_object.continent + ' is ' + country
        detail = 'The country that has the highest ' + field_display + ' in the world is ' + best_country['name'] + \
                 ' with value of ' + str(best_country['field_value'])
        real_or_fake = position == 1
    else:
        top_position = rank_top_fact(position, real_or_fake)

        fact = 'The country ' + country + ' is in the top ' + str(top_position) + ' in terms of ' + field_display + ' in ' + country_object.continent
        detail = 'The country ' + country + ' is ranked ' + str(position) + ' in ' + field_display + ' in ' + country_object.continent
    return {
        'topic': topic,
        'fact': fact,
        'hint':  'The country ' + country + ' has an ' + field_display + ' of ' + str(getattr(country_object, field)),
        'answer': real_or_fake,
        'detail': detail
    }

# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of given field.
def compare_field(topic: str, first: str, second: str, field: str, field_display: str):
    countries_data = CountriesData()
    first_country = countries_data.country_data(country=first)
    second_country = countries_data.country_data(country=second)
    if first_country is None or second_country is None:
        return None

    first_field = getattr(first_country, field)
    second_field = getattr(second_country, field)
    if first_field is None or second_field is None or first_field == -1 or second_field == -1:
        return None
    difference = abs(first_field - second_field)
    if type(first_field) is float:
        difference = float_display(difference)
    else:
        difference = str(int(difference))
    return {
        'topic': topic,
        'fact': 'the country ' + first + ' has a larger ' + field_display + ' then ' + second,
        'hint': 'The difference of their ' + field_display + ' is ' + difference,
        'answer': first_field > second_field,
        'detail': 'the country ' + first + ' has an ' + field_display + ' of ' + str(first_field) +
                  ' whereas the country ' + second + ' has an ' + field_display + ' of ' + str(second_field),
    }