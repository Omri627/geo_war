import datetime

from fastapi import HTTPException
from mysql.connector import DataError
from pydantic import BaseModel

from db.dal_quries.score_queries import ScoreQueries
from db.db_handler import DbHandler
from utils.const import Const


class Score(BaseModel):
    user_name: str
    country_code: str
    points: int
    date: str

    def insert_score(self):
        db_handler = DbHandler()
        try:
            data = {'user_name': self.user_name, 'country_code': self.country_code, 'points': self.points,
                    'date': datetime.datetime.strptime(self.date, Const().DATETIME_FORMAT), }

            db_handler.insert_one_to_table(ScoreQueries.FIELDS, ScoreQueries.INSERT_QUERY, data)
        except DataError:
            raise HTTPException(status_code=404, detail=f"user_name too long, max_length 20 character")
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"{e}")
