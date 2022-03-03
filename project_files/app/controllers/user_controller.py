
from fastapi import APIRouter
from app.models.user.user_in import UserIn
from app.models.user.user_out import UserOut
from app.services.user_service import add, delete, get_all, get_by_id, update


user_controller = APIRouter(
    prefix="/user",
    tags=["user-controller"]
)

# we are using our FastAPI instance and add a GET request endpoint for '/users', which mean getAllUsers in REST


@user_controller.get("s")
def get_users():
    return get_all()


# get user by id
@user_controller.get("/{id}", response_model=UserOut)
def get_user(id: int):
    return get_by_id(id)

# update the user


@user_controller.post("/{id}", response_model=UserIn, response_model_exclude={"password"})
def update_user(id: int, user: UserIn):
    return update(id, user)

# add a user to our collection


@user_controller.put("")
def add_user(user: UserIn):
    return add(user)

# delete an existing user


@user_controller.delete("/{id}")
def delete_user(id: int):
    return delete(id)
