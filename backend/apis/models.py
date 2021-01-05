from pydantic import BaseModel

class UserInput(BaseModel):
    username: str
    password: str

class Score(BaseModel):
    user_name: str
    country_code: str
    points: int
    date: str
