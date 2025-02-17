from facts.geography import *
from facts.religion import *
from facts.society import *
from facts.sport import *
from facts.economy import *
from db.models.country_fact import CountryFactCreator
from db.models.comparison_fact import ComparisonFactCreator
import random

class FactsGenerator:
    def __init__(self, user_country, rival_country):
        self.facts_limit = 4

        # priority facts
        self.priority = [
            ComparisonFactCreator(creator=compare_area, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_population, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=cities_larger_country, user_country=user_country, rival_country=rival_country),
            CountryFactCreator(creator=rank_population, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_area, country=rival_country, real_or_fake=random.choice([True, False])),
            ComparisonFactCreator(creator=compare_common_religion, user_country=user_country, rival_country=rival_country),
        ]

        # geography facts
        self.geography = [
            CountryFactCreator(creator=is_capital, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=most_populated, country=rival_country, real_or_fake=random.choice([True, False])),
            ComparisonFactCreator(creator=cities_larger_country, user_country=user_country, rival_country=rival_country),
            CountryFactCreator(creator=rank_populated_city, country=rival_country, real_or_fake=random.choice([True, False])),
            ComparisonFactCreator(creator=is_same_continent, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_area, user_country=user_country, rival_country=rival_country),
            CountryFactCreator(creator=rank_area, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=has_more_cities_then, country=rival_country, real_or_fake=random.choice([True, False])),
            ComparisonFactCreator(creator=compare_cities_quantity, user_country=user_country, rival_country=rival_country),
            CountryFactCreator(creator=continent_quantity, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_area_continent, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_populated_city_continent, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=evaluate_population, country=rival_country, real_or_fake=random.choice([True, False]))
        ]

        # religions facts
        self.religion = [
            CountryFactCreator(creator=religion_above_percentage, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=is_common_religion, country=rival_country, real_or_fake=random.choice([True, False])),
            ComparisonFactCreator(creator=compare_common_religion, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_main_religions, user_country=user_country, rival_country=rival_country),
            CountryFactCreator(creator=more_common_religion, country=rival_country, real_or_fake=random.choice([True, False])),
        ]

        # ethnic groups facts
        self.ethnic_groups = [
            ComparisonFactCreator(creator=compare_main_groups, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_ethnics_proportion, user_country=user_country, rival_country=rival_country),
            CountryFactCreator(creator=ethnic_above_percentage, country=rival_country, real_or_fake=random.choice([True, False])),
            ComparisonFactCreator(creator=compare_common_ethnic, user_country=user_country, rival_country=rival_country),
        ]

        # society facts
        self.society = [
            ComparisonFactCreator(creator=compare_unemployment_rate, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_area, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_population, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_life_expectancy, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_male_expectancy, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_female_expectancy, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_median_age, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_male_median_age, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_female_median_age, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_birth_rate, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_death_rate, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_internet_users, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_cellular_subscriptions, user_country=user_country, rival_country=rival_country),
            CountryFactCreator(creator=compare_birth_death_rate, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=compare_male_female_expectancy, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=compare_male_female_median, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=age_range_compare, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_population, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_unemployment_rate, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_median_age, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_expectancy_age, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_birth_rate, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_death_rate, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_internet_users, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_population_continent, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_expectancy_age_continent, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_unemployment_rate_continent, country=rival_country, real_or_fake=random.choice([True, False])),
        ]

        # sport facts
        self.sport = [
            CountryFactCreator(creator=most_players_country_league, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=count_players_country_leagues, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_players_quantity, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=country_players_quantity, country=rival_country, real_or_fake=random.choice([True, False])),
        ]

        # economy facts
        self.economy = [
            ComparisonFactCreator(creator=compare_revenues, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_expenditures, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_imports, user_country=user_country, rival_country=rival_country),
            ComparisonFactCreator(creator=compare_exports, user_country=user_country, rival_country=rival_country),
            CountryFactCreator(creator=rank_revenues, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_expenditures, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_imports, country=rival_country, real_or_fake=random.choice([True, False])),
            CountryFactCreator(creator=rank_exports, country=rival_country, real_or_fake=random.choice([True, False])),
        ]

        # facts groups
        self.facts_groups = [
            self.priority * 5, self.geography * 4, self.society * 4, self.sport * 3, self.religion * 2,
            self.ethnic_groups * 2, self.economy
        ]

    def select_fact(self):
        fact_groups_selected = random.choice(self.facts_groups)
        fact_creator = random.choice(fact_groups_selected)
        return fact_creator

    def battle_facts(self):
        facts = []
        facts_types = set()
        facts_quantity = 0
        while facts_quantity < self.facts_limit:
            # select a new fact type
            current_fact = self.select_fact()

            # prevent duplicate facts
            if current_fact in facts_types:
                continue
            else:
                facts_types.add(current_fact)

            # build current fact
            current_fact = current_fact.create()

            # add into facts set of the battle
            if current_fact is not None:
                facts.append(current_fact)
                facts_quantity += 1

        # returns set of facts for the battle
        return facts
