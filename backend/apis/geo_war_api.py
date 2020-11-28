from fastapi import FastAPI, status

from apis.user import User

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/}", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    user.create_user()
