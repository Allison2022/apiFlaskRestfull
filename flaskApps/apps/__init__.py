from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from apps.user.views import user

app.register_blueprint(user)