from fastapi import FastAPI

from apis.user import User

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/{user}")
def create_user(user: User):
    return {"user_name": user.user_name, "user_pass": user.password}
