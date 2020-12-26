
from pydantic import BaseModel
from db.dal_queries.user_queries import UserQueries
from db.db_handler import DbHandler

class User(BaseModel):
    username: str
    password: str
    email: str

class UserBuild():
    username: str
    password: str
    email: str
    def __init__(self, record: tuple):
        self.username = record[0]
        self.email = record[1]
        self.password = record[2]
        print(self.username, self.email, self.password)
    
    def build(self):
        return User(username=self.username, email=self.email, password=self.password)