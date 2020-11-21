class ReligionsQueries:
    ETHNICS_FIELDS = (
        'country_code', 'religion', 'percentage')

    INSERT_QUERY = '''
        INSERT INTO religions (country_code, religion, percentage)
            VALUES (%s, %s, %s)
    '''
