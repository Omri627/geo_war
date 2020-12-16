from db.business_logic.countries import CountriesData
from db.business_logic.sport import SportData


# most_players_country_league
# the method receives country name of league, and boolean variable indicate whether to build a true fact of fake
# and construct a fact that claims that the most players played in the given league is from X country
# the player should determine whether it is true or false
def most_players_country_league(league:str, real_or_fake: bool):
    sport_data = SportData()
    countries = sport_data.count_countries_players_league(league)
    if real_or_fake:
        index = 1
    else:
        index = randint(2, len(countries))
    return {
        'topic': 'Sport', 
        'fact': 'The country with the most players in the country soccer ' + league + ' league is ' + countries[index][0] + ' (apart from ' + league + ')',
        'hint': 'There are ' + countries[1][1] + ' players of the country with most players in ' + league + ' league',
        'answer': real_or_fake,
        'detail': 'The number of cities in the country ' + country + ' is ' + str(quantity)
    }

# count_players_country_leagues
# the method receives country name of league, and boolean variable indicate whether to build a true fact of fake and
# construct a fact that claims that the league with the highest number of player from the given country is of X country
# the player should determine whether it is true or false
def count_players_country_leagues(country: str, real_or_fake: bool):
    sport_data = SportData()
    countries = sport_data.count_country_players_leagues(country)
    if real_or_fake:
        index = 1
    else:
        index = randint(2, len(countries))
    return {
        'topic': 'Sport', 
        'fact': 'The league with the most number of players from the country ' + country + ' is ' + countries[index][0] + ' (apart from league of country ' + country + ')',
        'hint': 'In the League with most players of the ' + country + ' has ' + countries[1][1] + ' players of that country in total',
        'answer': real_or_fake,
        'detail': 'The League with most players of the ' + country + ' is ' + countries[1][0] ' and has ' + countries[1][1] + ' players of that country in total',
    }

# rank_players_quantity
# the method receives country name of league, and boolean variable indicate whether to build a true fact of fake and
# construct a fact that claims that the given country is ranked in top X in the number of players of the country in fifa soccer game 
# the player should determine whether it is true or false
def rank_players_quantity(country: str, real_or_fake: bool):
    sport_data = SportData()
    rank = sport_data.rank_players_quantity(country)
    if rank == 1:
        fact = 'The country with the most players in fifa is ' + country
        detail = fact + ' with number of players of ' # need to add
    else:
        if real_or_fake:
            top_position = rank - (rank % 10) + 10
        else:
            top_position = rank - (rank % 10) 
        fact = 'the country is ranked in top ' + str(top_position) + ' in the number of players in fifa soccer game'
        detail = 'the country is ranked ' + str(rank) + ' in the number of players in fifa soccer game'
    return {
        'topic': 'Sport', 
        'fact': fact,
        'hint': '',
        'answer': real_or_fake,
        'detail': detail,
    }