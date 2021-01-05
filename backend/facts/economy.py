from db.business_logic.countries import CountriesData


############## facts: compare countries fields ##########################

# compare_field
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in terms of given field.
def compare_field(first: str, second: str, field: str):
    countries_data = CountriesData()
    first_country = countries_data.country_data(country=first)
    second_country = countries_data.country_data(country=second)
    if first_country is None or second_country is None:
        return None

    first_field = getattr(first_country, field)
    second_field = getattr(second_country, field)
    return {
        'topic': 'Economy', 
        'fact': 'The country ' + first + ' has a higher ' + field + ' then ' + second,
        'hint': 'The difference of their ' + field + ' is ' + str(abs(first_field - second_field)),
        'answer': first_field > second_field,
        'detail': 'the country ' + first + ' has an ' + field + ' of ' + str(first_field) + " whereas the country " + second + " has an " + field + " of " + str(second_field),
    }

# compare_revenues
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total revenues.
def compare_revenues(first: str, second: str):
    field = 'revenues'
    return compare_field(first, second, field)

# compare_expenditures
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total expenditures.
def compare_expenditures(first: str, second: str):
    field = 'expenditures'
    return compare_field(first, second, field)

# compare_imports
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total imports.
def compare_imports(first: str, second: str):
    field = 'imports'
    return compare_field(first, second, field)

# compare_exports
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total exports.
def compare_exports(first: str, second: str):
    field = 'exports'
    return compare_field(first, second, field)
