from db.dal_queries.table_queries import TableQueries


class EthnicsQueries(TableQueries):
    # List of field in ethnics data table
    FIELDS = (
        'country_code', 'name', 'percentage')

    # Insert a new record into ethnics table
    INSERT_QUERY = '''  
        INSERT INTO ethnics (country_code, name, percentage)
            VALUES (%s, %s, %s)
    '''

    # Query: Get list of ethnics groups in given country
    # Format: [0] name of the country
    ETHNICS_COUNTRY = '''
        SELECT countries.name, ethnics.name, ethnics.percentage
        FROM ethnics, countries
        WHERE countries.code = ethnics.country_code AND countries.name = '%s'
    '''

    # Query: Get the main ethnic group in given country
    # Format: [0] name of the country
    MAIN_ETHNIC_COUNTRY = '''
        SELECT countries.name, ethnics.name, ethnics.percentage
        FROM ethnics, countries
        WHERE countries.code = ethnics.country_code AND countries.name = '%s'
        ORDER BY percentage DESC
        LIMIT 1
    '''
    
    # Query: Get common ethnics groups between two countries.
    # Format: [0] first country name, [1] second country name
    COMMON_ETHNICS = '''
        SELECT e1.name, e1.percentage, e2.percentage
        FROM ethnics as e1, countries as c1, ethnics as e2, countries as c2
        WHERE c1.code = e1.country_code AND c1.name = '%s' AND c2.code = e2.country_code AND c2.name = '%s' AND e1.name = e2.name
    '''

