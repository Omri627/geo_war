from fastapi import FastAPI, status
from db.models.user import User
from db.business_logic.countries import CountriesData
from db.business_logic.user import UserApi
from starlette.middleware.cors import CORSMiddleware
from apis.models import *
from facts.generator import FactsGenerator
from facts.geography import continent_quantity, rank_populated_city, has_more_cities_then
from facts.society import rank_population_continent, compare_population
from activator.activator import Activator

app = FastAPI()
activator = Activator()

origins = [
    "http://localhost",
    "localhost:4200",
    "http://localhost:4200",
    "https://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


@app.get("/")
def read_root():
    return activator.activate(method=compare_population, arguments=('Israel', 'Spain'))

# return list of countries the user can select to play with
@app.get("/countries/select")
def countries_select():
    countries_data = CountriesData()
    limit = 40
    select_method = countries_data.pick_options_countries
    arguments = (limit,)
    return activator.activate(method=select_method, arguments=arguments)


# returns list of countries competed in the game
@app.get("/countries/game/{selected_country}")
def countries_game(selected_country: str):
    countries_data = CountriesData()
    game_countries = countries_data.game_countries
    arguments = (selected_country,)
    return activator.activate(method=game_countries, arguments=arguments)


# create new user
@app.post("/users", status_code=status.HTTP_200_OK)
def create_user(user: User):
    user_api = UserApi()
    create_user = user_api.create_user
    arguments = (user,)
    valid, error = activator.activate(method=create_user, arguments=arguments)
    return {
        'valid': valid,
        'error_message': error 
    }


# check whether the username is already exist
@app.get("/users/exist/{username}")
def is_exist(username: str):
    user_api = UserApi()
    is_user_exist = user_api.is_exist
    arguments = (username,)
    return activator.activate(method=is_user_exist, arguments=arguments)


# check wether the username and password applied is valid
@app.post("/users/login", status_code=status.HTTP_200_OK)
def login(user: UserInput):
    user_api = UserApi()
    login_method = user_api.login
    arguments = (user.username, user.password)
    return activator.activate(method=login_method, arguments=arguments)


# return statics data of the user such as number of wins, total number of points and more.
@app.get("/user/statics/{username}")
def user_statics(username: str):
    user_api = UserApi()
    user_statics_method = user_api.user_statics
    arguments = (username,)
    return activator.activate(method=user_statics_method, arguments=arguments)


# returns the countries the user played with along with number of times he play with it in game
@app.get("/user/countries/{username}")
def user_countries(username: str):
    user_api = UserApi()
    user_countries_method = user_api.user_countries
    arguments = (username,)
    return activator.activate(method=user_countries_method, arguments=arguments)


# returns the user scores in the game.
@app.get("/user/scores/{username}")
def user_scores(username: str):
    user_api = UserApi()
    user_scores_summary = user_api.scores_summary
    arguments = (username,)
    return activator.activate(method=user_scores_summary, arguments=arguments)


# returns the user credentials/basic information
@app.get("/user/credentials/{username}", response_model=User, response_model_exclude={ 'password' })
def user_credentials(username: str):
    user_api = UserApi()
    user_credentials_method = user_api.user_credentials
    arguments = (username,)
    return activator.activate(method=user_credentials_method, arguments=arguments)


# returns the score of user latest game.
@app.get("/user/latest/{username}")
def user_latest_game(username: str):
    user_api = UserApi()
    user_latest_game_method = user_api.user_latest_game
    arguments = (username,)
    return activator.activate(method=user_latest_game_method, arguments=arguments)


# generate a list of facts for the battle
@app.get("/facts/{my_country}/vs/{rival_country}")
def battle_facts(my_country: str, rival_country:str):
    generator = FactsGenerator(user_country=my_country, rival_country=rival_country)
    get_facts = generator.battle_facts
    return activator.activate(method=get_facts, arguments=None)


# save a new game score
@app.post("/score/save", status_code=status.HTTP_201_CREATED)
def insert_score(score: ScoreInput):
    user_api = UserApi()
    insert_score_method = user_api.insert_score
    arguments = (score,)
    return activator.activate(method=insert_score_method, arguments=arguments)


# returns the players which gain the most total number of points
@app.get("/top/users/{limit}")
def top_users(limit: int):
    user_api = UserApi()
    top_ranking = user_api.top_users
    arguments = (limit,)
    return activator.activate(method=top_ranking, arguments=arguments)

# delete a game score
@app.delete("/delete/game/{id}")
def delete_game_score(id: int):
    user_api = UserApi()
    delete_game_score_method = user_api.delete_score_game
    arguments = (id,)
    return activator.activate(method=delete_game_score_method, arguments=arguments)


