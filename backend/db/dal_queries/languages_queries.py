from db.dal_queries.table_queries import TableQueries


class LanguagesQueries(TableQueries):
    # List of fields of languages data table 
    FIELDS = (
        'country_code', 'language', 'percentage')

    # Insert a new record into languages table
    INSERT_QUERY = '''
        INSERT INTO languages (country_code, language, percentage)
            VALUES (%s, %s, %s)
    '''
    
    # Query: Get official language of given country
    # format:  [0] name of the country
    OFFICIAL_LANGUAGE = '''
        SELECT languages.language
        FROM languages, countries
        WHERE languages.country_code = countries.code AND countries.name = '%s'
        ORDER BY percentage DESC
        LIMIT 1
    '''

    # Query: Get all languages of given country
    # format: [0] name of country
    LANGUAGES_COUNTRY = '''
        SELECT countries.name, languages.language, languages.percentage
        FROM languages, countries
        WHERE languages.country_code = countries.code AND countries.name = '%s'
    '''

    # Query: Get all common of two given countries
    # format: [0] name of first country, [1] name of second country
    COMMON_LANGUAGES = '''
        SELECT l1.language, l1.percentage, l2.percentage
        FROM languages as l1, countries as c1, languages as l2, countries as c2
        WHERE l1.country_code = c1.code AND l2.country_code = c2.code AND c1.name = 'Chile' AND c2.name = 'Cyprus'
	        AND l1.language = l2.language
    '''
