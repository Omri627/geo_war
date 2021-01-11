from db.business_logic.countries import CountriesData
from db.business_logic.sports import SportData
from db.business_logic.utils import rank_top_fact
import random

# most_players_country_league
# the method receives country name of league, and boolean variable indicate whether to build a true fact of fake
# and construct a fact that claims that the most number of players played in the given league is from X country
# the player should determine whether it is true or false
def most_players_country_league(league: str, real_or_fake: bool):
    if league not in ['Italy', 'Germany', 'France', 'United Kingdom', 'England', 'Spain']:
        return None

    # get number of players for each country played in this league
    sport_data = SportData()
    countries_league = sport_data.count_countries_players_league(league)
    if countries_league is None or len(countries_league) < 2:
        return None

    if real_or_fake:
        index = 1
    else:
        index = random.randint(2, len(countries_league) - 1)

    return {
        'topic': 'Sport', 
        'fact': 'The country with the most number of players in the ' + league + ' soccer league is ' +
                countries_league[index]['country'] + ' (of course, apart from ' + league + ' itself )',
        'hint': 'There are ' + str(countries_league[1]['players_quantity']) +
                ' players in total for the most common nationality in ' + league + ' league',
        'answer': real_or_fake,
        'detail': 'The country with the most number of players in ' + league + ' soccer league is '
                  + countries_league[1]['country'] + ' which contains in total ' +
                  str(countries_league[1]['players_quantity']) + ' players (apart from ' + league + ')'
    }


# count_players_country_leagues
# the method receives country name of league, and boolean variable indicate whether to build a true fact of fake and
# construct a fact that claims that the league with the highest number of player from the given country is of X country
# the player should determine whether it is true or false
def count_players_country_leagues(country: str, real_or_fake: bool):
    sport_data = SportData()
    countries = sport_data.count_country_players_leagues(country)
    if countries is None or len(countries) < 2:
        return None

    if country in ['Italy', 'Spain', 'Germany', 'France', 'England', 'United Kingdom']:
        most_country = 1
        index = 1 if real_or_fake else random.randint(2, len(countries) - 1)
    else:
        most_country = 0
        index = 0 if real_or_fake else random.randint(1, len(countries) - 1)
    print(most_country)

    return {
        'topic': 'Sport', 
        'fact': 'The league with the most number of players from ' + country + ' is ' +
                countries[index]['country'] + ' (apart from ' + country + ' local soccer league)',
        'hint': 'The League with most number of players from the country ' + country + ' has in total ' +
                str(countries[most_country]['players_quantity']) + ' players from this country',
        'answer': real_or_fake,
        'detail': 'The League with most number of players from the country ' + country + ' is ' + countries[most_country]['country']
                + ' which has ' + str(countries[most_country]['players_quantity']) + ' ' + country + ' players in total'
    }


# rank_players_quantity
# the method receives country name of league, and boolean variable indicate whether to build a true fact of fake and
# construct a fact that claims that the given country is ranked in top X in the number of players of the country in fifa soccer game 
# the player should determine whether it is true or false
def rank_players_quantity(country: str, real_or_fake: bool):
    sport_data = SportData()
    rank = sport_data.rank_players_quantity(country)
    players_quantity = sport_data.players_quantity(country)

    if rank == 1:
        fact = 'The country with the most number of players in FIFA soccer game is ' + country
        detail = fact + ' who contain ' + str(players_quantity) + ' players in total'
    else:
        top_position = rank_top_fact(position=rank, real_or_fake=real_or_fake)
        fact = 'The country ' + country + ' is ranked in top ' + str(top_position) + \
               ' in the number of players who appear in FIFA soccer game'
        detail = 'The country is ranked ' + str(rank) + ' in the number of players appearing in fifa soccer game'
    return {
        'topic': 'Sport', 
        'fact': fact,
        'hint': 'The number of players of ' + country + ' nationality appearing in FIFA soccer game is ' + str(players_quantity),
        'answer': real_or_fake,
        'detail': detail,
    }

# country_players_quantity
# the method receives country name of league, and boolean variable indicate whether to build a true fact of fake and
# construct a fact that claims that the number of players of given country is more then X in fifa soccer game
# the player should determine whether it is true or false
def country_players_quantity(country: str, real_or_fake: bool):
    # count number of players of given country nationality
    sport_data = SportData()
    players_quantity = sport_data.players_quantity(country)

    # compute the number of players appeared in the statement
    possible_options = [3, 5, 10, 20, 50, 100, 250, 500, 750, 1000, 1250, 1500, 1750, 2000]
    options_quantity = len(possible_options)
    index = 0
    while index < options_quantity and players_quantity > possible_options[index]:
        index += 1
    if real_or_fake:
        index -= 1

    # define fact and hint statements according to the quantity of players
    if index < 0:
        fact = 'There is no players of ' + country + ' nationality in Fifa soccer game'
        hint = 'There is no more then 3 players of ' + country + ' nationality in Fifa soccer game'
        real_or_fake = players_quantity == 0
    else:
        fact = 'The number of players of ' + country + ' nationality in Fifa soccer game is more then ' + str(possible_options[index])
        if index == 0:
            hint = 'The number of players of ' + country + ' nationality is less then 3'
        else:
            hint = 'The number of players is above ' + str(possible_options[index - 1])

    return {
        'topic': 'Sport',
        'fact': fact,
        'hint': hint,
        'answer': real_or_fake,
        'detail': 'The number of players of ' + country + ' nationality who appear in FIFA soccer game is ' + str(players_quantity),
    }
