
from app.models.user.user_in import UserIn
from app.repositories.user_repository import (add_user, delete_user,
                                              get_all_users, get_user_by_id,
                                              update_user)
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def get_by_id(id: int):
    try:
        return get_user_by_id(id)
    except:
        raise HTTPException(
            status_code=400, detail=f'User with id : {id} not found')


def get_all():
    return JSONResponse(status_code=200, content=get_all_users())


def update(id: int, user: UserIn):
    try:
        if(get_user_by_id(id) is None):
            raise HTTPException(
                status_code=400, detail=f'User with id : {id} not found')
        update_user(id, user)
        return user
    except:
        raise HTTPException(
            status_code=400, detail=f'Not able to update user with id {id}')


def add(user: UserIn):
    add_user(user)
    return JSONResponse(status_code=200, content=jsonable_encoder(user))


def delete(id: int):
    if(get_user_by_id(id) is None):
        raise HTTPException(
            status_code=400, detail=f'Impossible to delete User with id : {id} not found')
    delete_user(id)
    return JSONResponse(status_code=200, content={"isDeleted": True})
