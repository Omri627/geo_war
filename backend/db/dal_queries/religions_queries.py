from db.dal_queries.table_queries import TableQueries


class ReligionsQueries(TableQueries):
    # List of fields of religions table
    FIELDS = (
        'country_code', 'religion', 'percentage')

    # Insert a new record into religions data table
    INSERT_QUERY = '''
        INSERT INTO religions (country_code, religion, percentage)
            VALUES (%s, %s, %s)
    '''

    # Query: get a list of religions exist in particular country
    # Format: [0] name of the country 
    COUNTRY_RELIGIONS = '''
        SELECT religions.religion, religions.percentage
        FROM religions, countries
        WHERE religions.country_code = countries.code AND countries.name = '%s'
        ORDER BY religions.percentage DESC
    '''

    # Query: Get the most common religion in particular country
    # Format: [0] name of the country 
    MOST_COMMON_COUNTRY_RELIGION = '''
        SELECT religions.religion, religions.percentage
        FROM religions, countries
        WHERE religions.country_code = countries.code AND countries.name = '%s'
        ORDER BY religions.percentage DESC
        LIMIT 1
    '''


