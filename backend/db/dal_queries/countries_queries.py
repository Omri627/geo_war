from db.dal_queries.table_queries import TableQueries

class CountriesQueries(TableQueries):
    # List of field of Countries data table
    FIELDS = (
        'code', 'name', 'area', 'population', 'nationality', 'birth_rate', 'death_rate', 'cellular_subscriptions',
        'internet_users', 'crime_index', 'health_care', 'quality_of_life', 'lat', 'lon',
        '0_14_years', '15_24_years', '25_54_years', '55_64_years', '65_over', 'total_median_age', 'female_median_age',
        'male_median_age', 'male_expectancy', 'female_expectancy', 'total_expectancy', 'gdp', 'unemployment_rate',
        'revenues', 'expenditures', 'imports', 'exports', 'cost_of_living', 'continent')

    # Query: insert into countries table a new country record 
    INSERT_QUERY = '''
        INSERT INTO countries (code, name, area, population, nationality, birth_rate, death_rate,
        cellular_subscriptions, internet_users, crime_index, health_care, quality_of_life, lat,
        lon, 0_14_years, 15_24_years, 25_54_years, 55_64_years, 65_over, total_median_age, female_median_age,
        male_median_age, male_expectancy, female_expectancy, total_expectancy, gdp, unemployment_rate, revenues,
        expenditures, imports, exports, cost_of_living, continent)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    # Query: Get a detailed information about a praticular country from table
    COUNTRY_DATA = '''
        SELECT * FROM countries
        WHERE countries.name = '%s'
    '''

    # Query: Get population density of given country
    # format: [0] name of the country
    POPULATION_DENSITY  = '''
        SELECT countries.population / countries.area as population_density  
        FROM geo_data.countries
        WHERE countries.name = '%s'
    '''

    # Query: Get the names of the countries which gains the largest values of given field
    # format: [0] field name  [1] number of countries in the list
    MOST_FIELD = '''
        SELECT countries.name, countries.%s
        FROM countries
        ORDER BY %s DESC
        LIMIT %d
    '''

    # format: [1] continent name [0, 2] field name  [3] number of countries in the list
    MOST_FIELD_CONTINENT = '''
        SELECT countries.name, countries.%s
        FROM countries
        WHERE countries.continent = '%s'
        ORDER BY %s DESC
        LIMIT %d
    '''

    # Query: Get the names of the countries which gains the smallest values of given field
    # format: [0] field name  [1] number of countries in the list
    LEAST_FIELD = '''
        SELECT countries.name
        FROM countries
        ORDER BY %s ASC 
        LIMIT %d
    '''

    # Query: Get the countries with the most population density
    # format: [0] the size of list 
    TOP_POPULATION_DENSITY = '''
        SELECT countries.name, countries.population / countries.area as population_density
        FROM countries
        GROUP BY countries.name
        ORDER BY population_density DESC
        LIMIT %d 
    '''

    # Query: Get the countries with the least population density
    # format: [0] the size of list 
    LEAST_POPULATION_DENSITY = '''
        SELECT countries.name, countries.population / countries.area as population_density
        FROM countries
        GROUP BY countries.name
        HAVING population_density > 0
        ORDER BY population_density ASC
        LIMIT %d 
    '''

    # Query: Get the rank of given country in terms of given field.
    # format: [0, 1] field name [2] name of the country
    RANK_COUNTRY_BY_FIELD = '''
        SELECT COUNT(*) + 1 quantity
        FROM countries
        WHERE countries.%s > (SELECT countries.%s FROM geo_data.countries WHERE countries.name = '%s')
    '''

    # Query: Get the rank of given country in terms of given field.
    # format: [0, 1] field name [2] name of the country
    RANK_COUNTRY_BY_POPULATION_DENSITY = '''
        SELECT COUNT(*) + 1 quantity
        FROM countries
        WHERE countries.population > 5000000 AND countries.area / countries.population > (SELECT countries.area / countries.population FROM geo_data.countries WHERE countries.name = '%s')
    '''

    # Query: Get fifteen random countries to compete in the game
    COUNTRIES_GAME = '''
        SELECT countries.name
        FROM countries
        ORDER BY rand() * countries.internet_users DESC
        LIMIT 15
    '''

    # update country with it continent
    UPDATE_COUNTRY_CONTINENT = '''
        UPDATE countries
        SET continent= '%s'
        WHERE code='%s'
    '''

    # Query: Get the rank of given country in terms of given field among the continents
    # format: [0] country name [1, 2] field name [3] country name
    RANK_COUNTRY_BY_FIELD_CONTINENT = '''
        SELECT COUNT(*) + 1 as quantity
        FROM countries
        WHERE countries.continent =  (SELECT countries.continent FROM geo_data.countries WHERE countries.name = '%s') AND countries.%s > (SELECT countries.%s FROM geo_data.countries WHERE countries.name = '%s')
    '''

    # Query: number of countries in the continent of given country
    # format: [0] country name
    COUNTRIES_QUANTITY_CONTINENT = '''
        SELECT COUNT(*) as quantity
        FROM countries
        WHERE countries.continent = (SELECT countries.continent FROM countries WHERE countries.name = '%s')
    '''

