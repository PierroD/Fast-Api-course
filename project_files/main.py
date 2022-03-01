from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

"""
    Fast API
"""
# create a FastAPI instance
app = FastAPI(
    title="PierroD - Beginner course",
    description=("Learn Fast API"),
    version="1.0.0",
    redoc_url="/swagger",
)


"""
    Fake data
"""

user0 = {"id": 0, "name": "user0", "password": "test0"}
user1 = {"id": 1, "name": "user1", "password": "test1"}
user2 = {"id": 2, "name": "user2", "password": "test2"}

users = [user0, user1, user2]


class User(BaseModel):
    id: int
    name: str
    password: str


"""
    API endpoints
"""

# we are using our FastAPI instance and add a GET request endpoint for '/users', which mean getAllUsers in REST
@app.get("/users")
def get_users():
    return users

# get user by id
@app.get("/user/{id}")
def get_user(id: int):
    return users[id]

# update the user
@app.post("/user/{id}")
def update_user(id: int, user: User):
    if(users[id] != None):
        users[id] = user
    return user

# add a user to our collection
@app.put("/user")
def add_user(user: User):
    users.append(user)
    return user

# delete an existing user
@app.delete("/user/{id}")
def delete_user(id: int):
    if(users[id] != None):
        users.pop(id)
    return True


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=4000, reload=True)
