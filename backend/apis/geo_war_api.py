from fastapi import FastAPI, status
from db.models.user import User
from db.business_logic.user import UserApi
from db.business_logic.countries import CountriesData
from db.business_logic.user import UserApi
from starlette.middleware.cors import CORSMiddleware
from apis.models import *
from facts.generator import FactsGenerator
from facts.geography import has_more_then
from apis.activator import Activator
import random

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
    return activator.activate(method=has_more_then, arguments=('Spain', True))


@app.get("/countries/select")
def countries_select():
    countries_data = CountriesData()
    limit = 99
    select_method = countries_data.top_populated_countries
    arguments = (limit,)
    return activator.activate(method=select_method, arguments=arguments)


@app.get("/countries/game")
def countries_game():
    countries_data = CountriesData()
    game_countries = countries_data.game_countries
    return activator.activate(method=game_countries, arguments=None)


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


@app.get("/users/exist/{username}")
def is_exist(username: str):
    user_api = UserApi()
    is_user_exist = user_api.is_exist
    arguments = (username,)
    return activator.activate(method=is_user_exist, arguments=arguments)


@app.post("/users/login", status_code=status.HTTP_200_OK)
def login(user: UserInput):
    user_api = UserApi()
    login_method = user_api.login
    arguments = (user.username, user.password)
    return activator.activate(method=login_method, arguments=arguments)


@app.get("/user/statics/{username}")
def user_statics(username: str):
    user_api = UserApi()
    user_statics_method = user_api.user_statics
    arguments = (username,)
    return activator.activate(method=user_statics_method, arguments=arguments)


@app.get("/user/countries/{username}")
def user_countries(username: str):
    user_api = UserApi()
    user_countries_method = user_api.user_countries
    arguments = (username,)
    return activator.activate(method=user_countries_method, arguments=arguments)


@app.get("/user/scores/{username}")
def user_scores(username: str):
    user_api = UserApi()
    user_scores_summary = user_api.scores_summary
    arguments = (username,)
    return activator.activate(method=user_scores_summary, arguments=arguments)


@app.get("/user/credentials/{username}", response_model=User, response_model_exclude={ 'password' })
def user_credentials(username: str):
    user_api = UserApi()
    user_credentials_method = user_api.user_credentials
    arguments = (username,)
    return activator.activate(method=user_credentials_method, arguments=arguments)


@app.get("/user/latest/{username}")
def user_latest_game(username: str):
    user_api = UserApi()
    user_latest_game_method = user_api.user_latest_game
    arguments = (username,)
    return activator.activate(method=user_latest_game_method, arguments=arguments)


@app.get("/facts/{my_country}/vs/{rival_country}")
def battle_facts(my_country: str, rival_country:str):
    generator = FactsGenerator(user_country=my_country, rival_country=rival_country)
    get_facts = generator.battle_facts
    return activator.activate(method=get_facts, arguments=None)



'''
@app.post("/score/", status_code=status.HTTP_201_CREATED)
def insert_score(score: Score):
    score.insert_score()
'''