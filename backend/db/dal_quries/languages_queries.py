class LanguagesQueries:
    ETHNICS_FIELDS = (
        'country_code', 'language', 'percentage')

    INSERT_QUERY = '''
        INSERT INTO languages (country_code, language, percentage)
            VALUES (%s, %s, %s)
    '''
