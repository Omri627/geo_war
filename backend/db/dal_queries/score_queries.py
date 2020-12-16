from db.dal_queries.table_queries import TableQueries


class ScoreQueries(TableQueries):
    # List of field of games table
    FIELDS = (
        'user_name', 'country_code', 'points', 'date')

    # Insert a new record into games table
    INSERT_QUERY = '''
        INSERT INTO games (user_name, country_code, points, date)
            VALUES (%s, %s, %s, %s)
    '''
