from pydantic import BaseModel


class UserInput(BaseModel):
    username: str
    password: str


class ScoreInput(BaseModel):
    user_name: str
    country: str
    points: int
    conquered: int
