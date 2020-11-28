from db.dal_quries.table_queries import TableQueries


class CitesQueries(TableQueries):
    FIELDS = (
        'country_code', 'name', 'population', 'lat', 'lot')

    INSERT_QUERY = '''
        INSERT INTO city (country_code, name, population, lat, lot)
            VALUES (%s, %s, %s, %s, %s)
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