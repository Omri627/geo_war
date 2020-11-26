from db.dal_quries.table_queries import TableQueries


class CapitalQueries(TableQueries):
    FIELDS = (
        'country_code', 'capital')

    INSERT_QUERY = '''
        INSERT INTO capital (country_code, capital)
            VALUES (%s, %s)
    '''
