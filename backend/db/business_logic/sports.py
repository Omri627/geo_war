from db.dal_queries.soccer_queries import SoccerQueries
from db.db_handler import DbHandler

class SportData():
    def __init__(self):
        self.db_handler = DbHandler()
    
    # given a country of a soccer league,
    # the method returns the number of players of each country in this specific league
    def count_countries_players_league(self, country: str):
        return self.db_handler.receive_data(SoccerQueries.COUNTRIES_IN_LEAGUE, country)

    # given a name of country,
    # the method returns the number of players of given country played in the different leagues.
    def count_country_players_leagues(self, country: str):
        return self.db_handler.receive_data(SoccerQueries.COUNTRY_IN_LEAGUES, country)

    # given country league and country of players,
    # the method returns list of all the players of given country in the given league.
    def players_country_league(self, country_players: str, country_league: str):
        return self.db_handler.receive_data(SoccerQueries.COUNTRY_PLAYERS_LEAGUE, (country_league, country_players))

    # given name of a country,
    # the method returns the rank of countries in terms of number of players of the country in fifa game
    def rank_players_quantity(self, country: str):
        result = self.db_handler.receive_data(SoccerQueries.COUNTRY_RANK_PLAYERS_QUANTITY, country)
        return int(result[0][0])