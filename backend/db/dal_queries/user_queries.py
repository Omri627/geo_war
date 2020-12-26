from db.dal_queries.table_queries import TableQueries


class UserQueries(TableQueries):
    # List of fields of user data table
    FIELDS = (
        'username', 'email', 'password')

    # Insert a new record into user table
    INSERT_QUERY = '''
        INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
    '''

    # Query: Check if username already exist
    IS_EXIST = '''
        SELECT * FROM users
        WHERE users.username = '%s'
    '''
