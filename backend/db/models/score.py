from pydantic import BaseModel


class Score():
    id: int
    user_name: str
    country_code: str
    points: int
    conquered: int
    date: str

    def __init__(self, record: tuple):
        self.id = record[0]
        self.user_name = record[1]
        self.country = record[3]
        self.date = record[2]
        self.points = record[4]
        self.conquered = record[5]