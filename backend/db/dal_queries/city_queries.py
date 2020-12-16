from db.dal_queries.table_queries import TableQueries

'''
    CitiesQueries class gathered a list of queries performed on data table Cities.
'''
class CitiesQueries(TableQueries):
    # List of fields of city table
    FIELDS = (
        'country_code', 'name', 'population', 'lat', 'lot')

    # Insert a new city into cities data table
    INSERT_QUERY = '''
        INSERT INTO city (country_code, name, population, lat, lot)
            VALUES (%s, %s, %s, %s, %s)
    '''

    # Query: Get a detailed information about a praticular city from table
    CITY_DATA = '''
        SELECT * FROM city 
        WHERE city.name = '%s'
    '''

    # Query: count the number of cities of particular country
    # format: [0] name of the country
    CITIES_IN_COUNTRY = '''
        SELECT COUNT(*) As quantity
        FROM city, countries
        WHERE city.country_code = countries.code and countries.name = '%s';
    '''

    # Query: get a list of most populated cities of particular country
    # Format: [0] name of the country, [1] limitation on the number of cities.
    BIGGEST_CITIES = '''
        SELECT city.name
        FROM countries, city
        WHERE countries.code = city.country_code AND countries.name = '%s'
        ORDER BY city.population DESC
        LIMIT %d
    '''

    # Query: get the position of the most populated city in given country among all the cities in the world.
    # format: [0] name of the country
    POSITION_POPULATED_CITY = '''
        SELECT count(*) + 1 quantity
        FROM countries, city
        WHERE countries.code = city.country_code AND
	        city.population > ( SELECT city.population FROM city, countries
			                    WHERE city.country_code = countries.code AND countries.name = '%s' 
						        ORDER BY city.population DESC LIMIT 1 )
    '''

    # Query: Get all the cities in given first country which has more (or close) population to population size of entire second given country 
    # format: [0] name of first country, [1] name of second country
    CITIES_LARGER_COUNTRY = '''
        SELECT city.name, city.population, city.population > other.population as bigger
        FROM countries, city, (SELECT countries.population FROM countries WHERE countries.name = '%s') as other
        WHERE countries.code = city.country_code AND countries.name = '%s'
            AND city.population > (other.population / 2)
    '''
    
    # Query: Get the top countries which has the highest population per city
    # format: [0] size of the list
    POPULATION_PER_CITY = '''
        SELECT c1.population / (SELECT COUNT(*) As quantity
                        FROM geo_data.city, geo_data.countries as c2
                        WHERE city.country_code = c2.code and c1.name = c2.name) as population_per_city
        FROM geo_data.countries as c1
        WHERE c1.name = '%s'
    '''

    # Query: Get the top countries which has the highest population per city
    # format: [0] size of the list
    TOP_POPULATION_PER_CITY = '''
        SELECT c1.name, c1.population / (SELECT COUNT(*) As quantity
                        FROM geo_data.city, geo_data.countries as c2
                        WHERE city.country_code = c2.code and c1.name = c2.name) as population_per_city
        FROM geo_data.countries as c1
        ORDER BY population_per_city DESC
        TOP %d
    '''


    
    """
    queries examples:
    
    1) count number of cites in each country
    SELECT country_code, COUNT(*)
    FROM city
    GROUP BY country_code;
    
    2) same as 1 but with name instead of codes
    SELECT countries.name, COUNT(*)
    FROM city INNER JOIN countries ON city.country_code = countries.code
    GROUP BY city.country_code;
    
    3) calculate avg population on cities
    SELECT countries.name, AVG(city.population) as avg_city_pop
    FROM city INNER JOIN countries ON city.country_code = countries.code
    GROUP BY city.country_code;
    
    4) calculate avg population on cities where country population is bigger then 100M order by avg_cit DESC
    SELECT countries.name, countries.population as country_pop, AVG(city.population) as avg_city_pop
    FROM city INNER JOIN countries ON city.country_code = countries.code
    GROUP BY city.country_code
    HAVING countries.population > 100000000 ORDER BY avg_city_pop DESC;
    """