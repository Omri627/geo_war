from db.dal_queries.table_queries import TableQueries

class CapitalQueries(TableQueries):
    # List of fields of capital table
    FIELDS = (
        'country_code', 'capital')

    # Insert a new capital city into capitals data table
    INSERT_QUERY = '''
        INSERT INTO capital (country_code, capital)
            VALUES (%s, %s)
    '''

    # Query: Get the capital city of praticular country
    # format: [0] name of the country
    CAPITAL_OF_COUNTRY = '''
        SELECT capital.capital
        FROM geo_data.countries, geo_data.capital
        WHERE countries.code = capital.country_code AND countries.name = '%s' 
    '''

    # Query: Get the population size of capital city of praticular country
    # format: [0] name of the country
    POPULATION_CAPITAL = '''
        SELECT city.population
        FROM countries, capital, city
        WHERE countries.code = capital.country_code AND city.name = capital.capital AND countries.name = '%s'
        ORDER BY city.population DESC
        LIMIT 1
    '''

    # Query: Get the most populated capital city
    # format: [0] number of capital cities in list
    MOST_POPULATED_CAPITALS = '''
        SELECT capital.capital, city.population
        FROM countries, capital, city
        WHERE countries.code = capital.country_code AND city.name = capital.capital
        ORDER BY city.population DESC
        LIMIT %d
    '''

    # Query: Get the position of capital city of given country in terms of population size among all the cities in the world
    # format: [0] name of the country
    POSITION_CAPITAL_ALL = '''
        SELECT count(*) + 1 quantity
        FROM countries, city
        WHERE countries.code = city.country_code AND
            city.population > ( SELECT city.population FROM countries, capital, city
                                WHERE countries.code = capital.country_code AND city.name = capital.capital AND countries.name = '%s'
                                ORDER BY city.population DESC LIMIT 1)
    '''

    # Query: Get the position of capital city of given country in terms of population size among all the capital cities in the world
    # format: [0] name of the country
    POSITION_CAPITAL_CAPITALS = '''
        SELECT count(*) + 1 quantity
        FROM countries, city, capital
        WHERE countries.code = city.country_code AND capital.capital = city.name AND
	        city.population > ( SELECT city.population FROM countries, capital, city
						        WHERE countries.code = capital.country_code AND city.name = capital.capital AND countries.name = 'Spain'
						        ORDER BY city.population DESC LIMIT 1)
    '''