class CountriesQueries:
    COUNTRIES_FILED = (
        'code', 'name', 'area', 'population', 'nationality', 'birth_rate', 'death_rate', 'cellular_subscriptions',
        'internet_users', 'crime_index', 'health_care', 'quality_of_life', 'lat', 'lon',
        '0_14_years', '15_24_years', '25_54_years', '55_64_years', '65_over', 'total_median_age', 'female_median_age',
        'male_median_age', 'male_expectancy', 'female_expectancy', 'total_expectancy', 'gdp', 'unemployment_rate',
        'revenues', 'expenditures', 'imports', 'exports', 'cost_of_living', 'continent')

    INSERT_QUERY = '''
        INSERT INTO countries (code, name, area, population, nationality, birth_rate, death_rate,
         cellular_subscriptions, internet_users, crime_index, health_care, quality_of_life, lat,
          lon, 0_14_years, 15_24_years, 25_54_years, 55_64_years, 65_over, total_median_age, female_median_age,
           male_median_age, male_expectancy, female_expectancy, total_expectancy, gdp, unemployment_rate, revenues,
            expenditures, imports, exports, cost_of_living, continent)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
             %s, %s, %s, %s, %s, %s, %s, %s)
    '''
