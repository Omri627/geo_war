from db.dal_quries.table_queries import TableQueries


class CitesQueries(TableQueries):
    FIELDS = (
        'country_code', 'name', 'population', 'lat', 'lot')

    INSERT_QUERY = '''
        INSERT INTO city (country_code, name, population, lat, lot)
            VALUES (%s, %s, %s, %s, %s)
    '''
