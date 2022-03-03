from app.models.user.user_in import UserIn


user0 = {"id": 0, "name": "user0", "password": "test0"}
user1 = {"id": 1, "name": "user1", "password": "test1"}
user2 = {"id": 2, "name": "user2", "password": "test2"}

users = [user0, user1, user2]


def get_all_users():
    return users


def get_user_by_id(id: int):
    return users[id]


def update_user(id: int, user: UserIn):
    users[id] = user


def add_user(user: UserIn):
    users.append(user)


def delete_user(id: int):
    users.pop(id)
