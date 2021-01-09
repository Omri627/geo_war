from db.dal_queries.user_queries import UserQueries
from db.dal_queries.score_queries import ScoreQueries
from db.db_handler import DbHandler
from db.models.user import User, UserBuild
from db.models.score import Score
from fastapi import HTTPException
from mysql.connector import IntegrityError, DataError
import datetime
import json
from apis.models import ScoreInput
import os

class UserApi():
    def __init__(self):
        self.db_handler = DbHandler()

    # receives a user object contains information about new user
    # the method insert the new user into user data table
    def create_user(self, user: User):
        db_handler = DbHandler()
        data = {'username': user.username, 'email': user.email, 'password': user.password}
        try:
            db_handler.insert_one_to_table(UserQueries.FIELDS, UserQueries.INSERT_QUERY, data)
            return True, "User account created successfully"
        except IntegrityError:
            return False, "User: " + user.username + " already exist"
        except DataError:
            return False, "user_name too long, max_length 20 character"
        except Exception as e:
            return False, str(e)
    
    # receives a username
    # the method returns a boolean variable indicate wether this username is already exist or not
    def is_exist(self, username: str):
        records = self.db_handler.receive_data(UserQueries.IS_EXIST, (username,))
        if len(records) > 0:
            return True
        return False

    # receives a username
    # the method returns basic details/credentials about the user.
    def user_credentials(self, username: str):
        records = self.db_handler.receive_data(UserQueries.IS_EXIST, (username,))
        if records is None or len(records) == 0:
            return None
        return UserBuild(records[0]).build()
    
    # receives a username and password
    # the method returns a boolean variable wether the credentials are correct
    def login(self, username: str, password: str):
        records = self.db_handler.receive_data(UserQueries.IS_EXIST, (username,))
        if records is None or len(records) == 0:
            return False
        user_record = records[0]
        if user_record[0] == username and user_record[2] == password:
            return True
        return False

    # receives a username
    # the method returns a summary/statics of the username games
    def user_statics(self, username: str):
        # activate statics queries
        try:
            top_country = self.db_handler.receive_data(ScoreQueries.TOP_COUNTRY_PLAYED, (username,))[0][0]
            games_played = self.db_handler.receive_data(ScoreQueries.USER_GAMES_PLAYED, (username,))[0][0]
            total_points = self.db_handler.receive_data(ScoreQueries.TOTAL_POINTS, (username,))[0][0]
            total_conquered = self.db_handler.receive_data(ScoreQueries.TOTAL_CONQUERED, (username,))[0][0]
            wins_quantity = self.db_handler.receive_data(ScoreQueries.WINS_QUANTITY, (username,))[0][0]
        except:
            top_country = '-'
            games_played = total_points = total_conquered = wins_quantity = 0
        # return combined data at json format
        return {
            'username': username,
            'top_country': top_country,
            'games_played': games_played,
            'total_points': total_points,
            'total_conquered': total_conquered,
            'wins_quantity': wins_quantity
        }
    
    # receives a username
    # returns the countries the user played with along with number of times he play with it in game
    def user_countries(self, username: str):
        countries = []
        records = self.db_handler.receive_data(ScoreQueries.COUNTRY_PLAYED, (username,))
        for record in records:
            countries.append({
                'country': record[0],
                'games_played': record[1]
            })
        return countries

    # receives a username and returns a summary of his games
    def scores_summary(self, username: str):
        scores = []
        records = self.db_handler.receive_data(ScoreQueries.USERNAME_SCORES, (username,))
        for record in records:
            scores.append(Score(record))
        return scores

    def user_latest_game(self, username: str):
        records = self.db_handler.receive_data(ScoreQueries.LATEST_GAME, (username,))
        if records is None or len(records) == 0:
            return None
        return Score(records[0])

    def insert_score(self, score: ScoreInput):
        db_handler = DbHandler()
        try:
            with open('./utils/name_code.json') as json_file:
                name_code = json.load(json_file)
                country_code = name_code[score.country]
                data = {'user_name': score.user_name, 'country_code': country_code, 'points': score.points,
                        'conquered': score.conquered, 'date': datetime.datetime.now()}
                db_handler.insert_one_to_table(ScoreQueries.FIELDS, ScoreQueries.INSERT_QUERY, data)
                return {'valid': True, 'error_message': ''}
        except DataError:
            return {'valid': False, 'error_message': "user_name too long, max_length 20 character"}
        except Exception as e:
            return {'valid': False, 'error_message': str(e)}

    def top_users(self, limit):
        top = []
        records = self.db_handler.receive_data(ScoreQueries.TOP_USERS, (limit,))
        for record in records:
            top.append({
                'username': record[0],
                'total_points': int(record[1]),
                'wins': record[2]
            })
        return top

    def delete_score_game(self, game_id):
        try:
            self.db_handler.delete_records(ScoreQueries.DELETE_GAME_SCORE, (game_id,))
            return {'valid': True, 'error_message': ''}
        except Exception as e:
            return {'valid': False, 'error_message': str(e)}