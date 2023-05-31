from flask import Blueprint
from flask_restful import Resource
from apps import api

user = Blueprint('user', __name__)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')