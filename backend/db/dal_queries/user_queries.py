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

    # Query: Update credentials of specific user
    # format: [0] new email address [1] new password [2] username
    UPDATE_USER_CREDENTIALS = '''
        UPDATE users
        SET users.email = '%s', users.password = '%s'
        WHERE users.username = '%s';
    '''