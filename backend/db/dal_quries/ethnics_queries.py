from db.dal_quries.table_queries import TableQueries


class EthnicsQueries(TableQueries):
    FIELDS = (
        'country_code', 'name', 'percentage')

    INSERT_QUERY = '''
        INSERT INTO ethnics (country_code, name, percentage)
            VALUES (%s, %s, %s)
    '''
