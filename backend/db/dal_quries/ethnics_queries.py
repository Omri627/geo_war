class EthnicsQueries:
    ETHNICS_FIELDS = (
        'code', 'name', 'ethnics')

    INSERT_QUERY = '''
        INSERT INTO ethnics (code, name, ethnics)
            VALUES (%s, %s, %s)
    '''
