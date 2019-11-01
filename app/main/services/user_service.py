#  Service file for User
# All the business logic for the user module is present here
from app.main.models.User import User
from app import bcrypt

def add_user(data):
    data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    new_user = User(data)
    new_user.insert()

def get_user(name):
    return User.fetch(name)


def get_all_users():
    return User.fetch_all_users()

def authenticateUser(username, password):
   
    print(User.fetch(username))
    if(bcrypt.check_password_hash(User.fetch(username)["password"], password)):
        return "TRUE"
    else:
        return "FALSE"
    



