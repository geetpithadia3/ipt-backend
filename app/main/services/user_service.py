from app.main.models.User import User


def add_user(data):
    new_user = User(name='GEET')
    new_user.insert()
    return '', 204


def get_user(name):
    return User.fetch(name)


def get_all_users():
    return User.fetch_all_users()


