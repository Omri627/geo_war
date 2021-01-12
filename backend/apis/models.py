from pydantic import BaseModel
from typing import Optional


class UserInput(BaseModel):
    username: str
    password: str
    email: Optional[str] = ''


class ScoreInput(BaseModel):
    user_name: str
    country: str
    points: int
    conquered: int
