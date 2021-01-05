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

    COMMON_COUNTRIES_RELIGIONS = '''
        SELECT r1.religion, r1.percentage, r2.percentage 
        FROM religions as r1, countries as c1, religions as r2, countries as c2
        WHERE c1.code = r1.country_code AND c1.name = '%s' AND c2.code = r2.country_code AND c2.name = '%s' AND r1.religion = r2.religion
    '''


