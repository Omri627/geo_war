from db.dal_queries.table_queries import TableQueries


class ScoreQueries(TableQueries):
    # List of field of games table
    FIELDS = (
        'user_name', 'country_code', 'points', 'conquered', 'date')

    # Insert a new record into games table
    INSERT_QUERY = '''
        INSERT INTO games (user_name, country_code, points, conquered, date)
            VALUES (%s, %s, %s, %s, %s)
    '''

    # Query: Get all scores/summary of game results of given user
    # format: [0] username
    USERNAME_SCORES = '''
        SELECT games.id, games.user_name, games.date, countries.name, games.points, games.conquered
        FROM games, countries
        WHERE games.country_code = countries.code and games.user_name = '%s';
    '''

    # Query: Get total sum of points of the user
    # format: [0] username
    TOTAL_POINTS = '''
        SELECT SUM(games.points) total_points
        FROM games
        WHERE games.user_name = '%s';
    '''

    # Query: Get total sum of conquered of the user
    # format: [0] username
    TOTAL_CONQUERED = '''
        SELECT SUM(games.conquered) total_conquered
        FROM games
        WHERE games.user_name = '%s';
    '''

    # Query: Get the number of games played by user
    # format: [0] username
    USER_GAMES_PLAYED = '''
        SELECT COUNT(*) as games_played
        FROM games
        WHERE games.user_name = '%s';
    '''

    # Query: Get the top country played by the user
    # format: [0] username
    TOP_COUNTRY_PLAYED = '''
        SELECT countries.name, COUNT(*) quantity
        FROM games, countries
        WHERE games.country_code = countries.code and games.user_name = '%s'
        GROUP BY countries.name
        ORDER BY quantity DESC
        LIMIT 1
    '''

    # Query: Get the countries played by the user
    # format: [0] username
    COUNTRY_PLAYED = '''
        SELECT countries.name, COUNT(*) quantity
        FROM games, countries
        WHERE games.country_code = countries.code and games.user_name = '%s'
        GROUP BY countries.name
        ORDER BY quantity DESC
    ''' 

    # Query: Get the latest game of particular user
    # format: [0] username
    LATEST_GAME = '''
        SELECT games.id, games.user_name, games.date, countries.name, games.points, games.conquered
        FROM games, countries
        WHERE games.country_code = countries.code and games.user_name = '%s'
        ORDER BY date DESC
        LIMIT 1
    '''

    # Query: top X users with largest number of points.
    # format [0] number of users (X)
    TOP_USERS = '''
        SELECT g1.user_name, SUM(g1.points) as total_points, (SELECT COUNT(g2.conquered) as wins FROM games as g2 WHERE g2.conquered > 14 AND g1.user_name = g2.user_name) as wins
        FROM games as g1 
        GROUP BY g1.user_name
        ORDER BY total_points DESC
        LIMIT %d
    '''

    # Query: number of wins of specific user
    # format: [0] user name
    WINS_QUANTITY = '''
        SELECT COUNT(games.conquered) 
        FROM games 
        WHERE games.conquered > 14 AND games.user_name = '%s'
    '''

    # Query: delete score record
    # format: [0] id of the game record
    DELETE_GAME_SCORE = '''
        DELETE FROM games
        WHERE games.id = %d
    '''