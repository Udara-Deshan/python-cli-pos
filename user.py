import json
import os

__db_location__ = "db"
__session_file__ = f"{__db_location__}/session.db"
__user_folder__ = f"{__db_location__}/user"


def init():
    db()


def db():
    os.makedirs(__user_folder__)


def __get_logged_user():
    f = open(__session_file__, "r")
    username = f.readline()
    return username


def view():
    username = __get_logged_user()
    print(username)


def login():
    user = User()
    username = input("Username : ")
    password = input("Password : ")
    user.find(username)
    if username == user.username:
        if password == user.password:
            print(user.username, " is login")
            f = open(__session_file__, "w")
            f.write(username)
            f.close
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")


def sing_up():
    user = User()
    user.username = input("Enter user name : ")
    user.password = input("Enter password : ")
    user.type = input("Enter user type is CUSTOMER or OWNER : ")
    user.save()


def set_command_and_params(command, params):
    if command == "init":
        init()
    elif command == "singup":
        sing_up()
    elif command == "login":
        login()
    elif command == "view":
        view()


class User:
    def __init__(self):
        self.type = None
        self.password = None
        self.username = None
        if os.path.exists(__user_folder__):
            pass
        else:
            init()

    def save(self):
        # user_id = self.last_id + 1
        _data_ = {
            "userName": self.username,
            "password": self.password,
            "usertype": self.type
        }

        with open(f"{__user_folder__}/{self.username}.db", "w") as item_file:
            json.dump(_data_, item_file)
        print(self.username, " is success added")

    def find(self, username):
        User.__get_item_by_path(self, f"{__user_folder__}/{username}.db")

    def __get_item_by_path(self, path):
        try:
            with open(path, "r") as user_file:
                _data_ = json.load(user_file)
                self.username = _data_["userName"]
                self.password = _data_["password"]
                self.type = _data_["usertype"]
        except FileNotFoundError:
            print("user is not exists")
