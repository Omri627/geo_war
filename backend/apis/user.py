from fastapi import HTTPException
from mysql.connector import IntegrityError, DataError
from pydantic import BaseModel

from db.dal_quries.user_queries import UserQueries
from db.db_handler import DbHandler


class User(BaseModel):
    user_name: str
    password: str

    def create_user(self):
        db_handler = DbHandler()
        data = {'user_name': self.user_name, 'password': self.password}
        try:
            db_handler.insert_one_to_table(UserQueries.FIELDS, UserQueries.INSERT_QUERY, data)
        except IntegrityError:
            raise HTTPException(status_code=404, detail=f"User: {self.user_name} already exist")
        except DataError:
            raise HTTPException(status_code=404, detail=f"user_name too long, max_length 20 character")
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"{e}")
