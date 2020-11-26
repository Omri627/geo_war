from db.dal_quries.table_queries import TableQueries


class LanguagesQueries(TableQueries):
    FIELDS = (
        'country_code', 'language', 'percentage')

    INSERT_QUERY = '''
        INSERT INTO languages (country_code, language, percentage)
            VALUES (%s, %s, %s)
    '''
