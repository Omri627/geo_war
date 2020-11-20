class EthnicsQueries:
    ETHNICS_FIELDS = (
        'country_code', 'name', 'percentage')

    INSERT_QUERY = '''
        INSERT INTO ethnics (country_code, name, percentage)
            VALUES (%s, %s, %s)
    '''
