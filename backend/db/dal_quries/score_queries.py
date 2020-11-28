from db.dal_quries.table_queries import TableQueries


class ScoreQueries(TableQueries):
    FIELDS = (
        'user_name', 'country_code', 'points', 'date')

    INSERT_QUERY = '''
        INSERT INTO scores (user_name, country_code, points, date)
            VALUES (%s, %s, %s, %s)
    '''
