from typing import Optional
from fastapi import HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse, FileResponse
from pydantic import BaseModel
import uvicorn
import os

"""
    Fast API
"""
# create a FastAPI instance
app = FastAPI(
    title="PierroD - Confirm course",
    description=("Learn Fast API"),
    version="1.0.0",
    redoc_url="/swagger",
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    # you can allow some routes / but here we are allowing all the existing routes
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
    Fake data
"""

user0 = {"id": 0, "name": "user0", "password": "test0"}
user1 = {"id": 1, "name": "user1", "password": "test1"}
user2 = {"id": 2, "name": "user2", "password": "test2"}

users = [user0, user1, user2]


class UserIn(BaseModel):
    id: int
    name: str
    password: Optional[str] = None


class UserOut(BaseModel):
    id: int
    name: str


"""
    API endpoints
"""

# we are using our FastAPI instance and add a GET request endpoint for '/users', which mean getAllUsers in REST
@app.get("/users")
def get_users():
    return JSONResponse(status_code=200, content=users)


# get user by id
@app.get("/user/{id}", response_model=UserOut)
def get_user(id: int):
    try:
        return users[id]
    except:
        raise HTTPException(
            status_code=400, detail=f'User with id : {id} not found')

# update the user
@app.post("/user/{id}", response_model=UserIn, response_model_exclude={"password"})
def update_user(id: int, user: UserIn):
    try:
        if(users[id] is None):
            raise HTTPException(
                status_code=400, detail=f'User with id : {id} not found')
        users[id] = user
        return user
    except:
        raise HTTPException(
            status_code=400, detail=f'Not able to update user with id {id}')


# add a user to our collection
@app.put("/user")
def add_user(user: UserIn):
    users.append(user)
    return JSONResponse(status_code=200, content=user)

# delete an existing user
@app.delete("/user/{id}")
def delete_user(id: int):
    if(users[id] is None):
        raise HTTPException(
            status_code=400, detail=f'Impossible to delete User with id : {id} not found')
    users.pop(id)
    return JSONResponse(status_code=200, content={"isDeleted": True})

# redirect url
@app.get("/url")
def get_url():
    try:
        print(os.getenv("MY_URL"))
        return RedirectResponse(os.getenv("MY_URL"))
    except:
        raise HTTPException(
            status_code=500, detail="Not able to load url from .env")


# return from .env
@app.get("/from_env")
def get_from_env():
    return os.getenv("MY_URL")

# return an image
@app.get("/image")
def get_image():
    return FileResponse("../images/minions.jpg")


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=4000, reload=True)
