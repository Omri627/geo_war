class SoccerQueries:
    SOCCER_FIELDS = (
        'country_code', 'player_name', 'team', 'position')

    INSERT_QUERY = '''
        INSERT INTO soccer (country_code, player_name, team, position)
            VALUES (%s, %s, %s, %s)
    '''
