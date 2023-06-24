from flask import Flask
from flask_restful import Api
# from apps.users.views import UserRestFull, UserRestFullList

app = Flask(__name__)
api = Api(app)

from apps.users.user import user
from apps.databases.database import database

app.register_blueprint(user)
app.register_blueprint(database)