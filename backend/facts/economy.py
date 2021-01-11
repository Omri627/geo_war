from db.business_logic.countries import CountriesData
from facts.general import compare_field, rank_field

############## facts: compare countries fields ##########################

# compare_revenues
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total revenues.
def compare_revenues(first: str, second: str):
    field = 'revenues'
    return compare_field('Economy', first, second, field, field)

# compare_expenditures
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total expenditures.
def compare_expenditures(first: str, second: str):
    field = 'expenditures'
    return compare_field('Economy', first, second, field, field)

# compare_imports
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total imports.
def compare_imports(first: str, second: str):
    field = 'imports'
    return compare_field('Economy', first, second, field, field)

# compare_exports
# the method receives two countries denoted as first and second and
# construct a fact which compare between the two countries in the total exports.
def compare_exports(first: str, second: str):
    field = 'exports'
    return compare_field('Economy', first, second, field, field)

############## facts: ranks #######################

def rank_revenues(country: str, real_or_fake: bool):
    return rank_field(topic='Economy', country=country, field='revenues', field_display='revenues', real_or_fake=real_or_fake)

def rank_expenditures(country: str, real_or_fake: bool):
    return rank_field(topic='Economy', country=country, field='expenditures', field_display='expenditures', real_or_fake=real_or_fake)

def rank_imports(country: str, real_or_fake: bool):
    return rank_field(topic='Economy', country=country, field='imports', field_display='imports', real_or_fake=real_or_fake)

def rank_exports(country: str, real_or_fake: bool):
    return rank_field(topic='Economy', country=country, field='exports', field_display='exports', real_or_fake=real_or_fake)
