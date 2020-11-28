from db.dal_quries.table_queries import TableQueries


class UserQueries(TableQueries):
    FIELDS = (
        'user_name', 'password')

    INSERT_QUERY = '''
        INSERT INTO users (user_name, password)
            VALUES (%s, %s)
    '''
