from fastapi import FastAPI, status
from db.models.user import User
from db.business_logic.user import UserApi
from facts.religion import above_percentage
from db.business_logic.countries import CountriesData
from db.business_logic.user import UserApi
from starlette.middleware.cors import CORSMiddleware
from apis.models import *
from facts.geography import has_more_then, is_capital, most_populated
import random

app = FastAPI()

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
    return above_percentage('Israel', False)
    #return {"Hello": "World"}

@app.get("/countries/select")
def countries_select():
    countries_data = CountriesData()
    return countries_data.top_populated_cities(limit=99)

@app.get("/countries/game")
def countries_game():
    countries_data = CountriesData()
    return countries_data.game_countries()

@app.post("/users", status_code=status.HTTP_200_OK)
def create_user(user: User):
    print('dasdasdas')
    user_api = UserApi()
    valid, error = user_api.create_user(user)
    return {
        'valid': valid,
        'error_message': error 
    }

@app.get("/users/exist/{username}")
def is_exist(username: str):
    user_api = UserApi()
    is_exist = user_api.is_exist(username)
    return is_exist


@app.post("/users/login", status_code=status.HTTP_200_OK)
def login(user: UserInput):
    user_api = UserApi()
    return user_api.login(username=user.username, password=user.password)

@app.get("/user/statics/{username}")
def user_statics(username: str):
    user_api = UserApi()
    return user_api.user_statics(username=username)

@app.get("/user/countries/{username}")
def user_countries(username: str):
    user_api = UserApi()
    return user_api.user_countries(username=username)

@app.get("/user/scores/{username}")
def user_scores(username: str):
    user_api = UserApi()
    return user_api.scores_summary(username=username)

@app.get("/user/credentials/{username}", response_model=User, response_model_exclude={ 'password' })
def user_credentials(username: str):
    user_api = UserApi()
    return user_api.user_credentials(username=username)

@app.get("/user/latest/{username}")
def user_latest_game(username: str):
    user_api = UserApi()
    return user_api.user_latest_game(username=username)

@app.get("/facts/{my_country}/vs/{rival_country}")
def battle_facts(my_country: str, rival_country:str):
    facts = []
    rand = random.choice([True, False])
    facts.append(has_more_then(rival_country, 100))
    facts.append(has_more_then(rival_country, 100))
    facts.append(has_more_then(rival_country, 100))
    facts.append(has_more_then(rival_country, 200))
    return facts



'''
@app.post("/score/", status_code=status.HTTP_201_CREATED)
def insert_score(score: Score):
    score.insert_score()
'''