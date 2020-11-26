from db.dal_quries.table_queries import TableQueries


class SoccerQueries(TableQueries):
    FIELDS = (
        'country_code', 'player_name', 'team', 'position')

    INSERT_QUERY = '''
        INSERT INTO soccer (country_code, player_name, team, position)
            VALUES (%s, %s, %s, %s)
    '''
