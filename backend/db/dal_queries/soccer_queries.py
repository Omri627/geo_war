from db.dal_queries.table_queries import TableQueries


class SoccerQueries(TableQueries):
    # List of fields of soccer data table
    FIELDS = (
        'country_code', 'player_name', 'team', 'position')

    # Insert a new record into soccer data table
    INSERT_QUERY = '''
        INSERT INTO soccer (country_code, player_name, team, position)
            VALUES (%s, %s, %s, %s)
    '''

    # Query: get the names of teams in given country league
    # format: [0] name of the country league
    COUTNRY_TEAMS = '''
        SELECT teams.team
        FROM teams, countries
        WHERE teams.country_code = countries.code AND countries.name = '%s'
    '''

    # Query: get the number of players of given nationality in fifa soccer game
    COUNTRY_PLAYERS_QUANTITY = '''
        SELECT COUNT(*) quantity
        FROM soccer, countries
        WHERE soccer.country_code = countries.code AND countries.name = '%s'
    '''

    # Query: the countries which has the most players in fifa
    # Format: [0] the number of countries in list
    MOST_PLAYERS_COUNTRY = '''
        SELECT countries.name, count(*) as quantity
        FROM soccer, countries
        WHERE soccer.country_code = countries.code
        GROUP BY countries.name
        ORDER BY quantity DESC
        LIMIT %d
    '''

    # Query: number of players of each country in specific league
    # format: [0] league country
    COUNTRIES_IN_LEAGUE = '''
        SELECT c1.name, count(*) quantity 
        FROM soccer, countries as c1
        WHERE soccer.country_code = c1.code AND soccer.team in
            (SELECT teams.team
            FROM teams, countries as c2
            WHERE teams.country_code = c2.code AND c2.name = '%s')
        GROUP BY c1.name
        ORDER BY quantity DESC
    '''

    # Query: how many players of given country played in the different leagues.
    # format: [0] name of the country
    COUNTRY_IN_LEAGUES = '''
        SELECT	countries.name, count(*) quantity
        FROM 	(SELECT * FROM soccer, countries
		         WHERE soccer.country_code = countries.code AND countries.name = '%s') as sport, teams, countries
        WHERE sport.team = teams.team AND teams.country_code = countries.code
        GROUP BY countries.name
        ORDER BY quantity DESC
    '''

    # Query: List of player names from given country who played in given league 
    # Format: [0] country of league, [1] country of players
    COUNTRY_PLAYERS_LEAGUE = '''
        SELECT soccer.player_name, soccer.team
        FROM teams, soccer, countries as c_team, countries as c_player
        WHERE teams.country_code = c_team.code AND soccer.country_code = c_player.code AND soccer.team = teams.team AND
	    c_team.name = '%s' AND c_player.name = '%s'
    '''

    # Query: Get the rank of given country in terms of number of players in fifa game.
    # format: [0] name of the country
    COUNTRY_RANK_PLAYERS_QUANTITY = '''
        SELECT COUNT(*) quantity
        FROM (  SELECT countries.name, count(*) as quantity
		        FROM soccer, countries
		        WHERE soccer.country_code = countries.code
		        GROUP BY countries.name
		        HAVING quantity >  (SELECT count(*) as quantity
					                FROM soccer, countries
					                WHERE soccer.country_code = countries.code AND countries.name = '%s')
		                            ORDER BY quantity DESC ) as ranks
    '''
