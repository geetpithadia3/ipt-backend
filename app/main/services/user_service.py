#  Service file for User
# All the business logic for the user module is present here
from app.main.models.User import User
from app import bcrypt

def add_user(data):
    data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    User.insert(data)

def get_user(email):
    return User.fetch(email)


def get_all_users():
    return User.fetch_all_users()

def authenticateUser(email, password):
    if(User.count_query({"email":email})==0):
        return 404
    elif(bcrypt.check_password_hash(User.fetch(email)["password"], password)):
        return 200
    else:
        return 204
    



