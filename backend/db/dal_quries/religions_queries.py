from db.dal_quries.table_queries import TableQueries


class ReligionsQueries(TableQueries):
    FIELDS = (
        'country_code', 'religion', 'percentage')

    INSERT_QUERY = '''
        INSERT INTO religions (country_code, religion, percentage)
            VALUES (%s, %s, %s)
    '''
