import json
from flask import Blueprint, request
from flask_restful import Resource
# from config import redis_manager, mongo
from apps import api

user = Blueprint('user', __name__)

class UserRestFull(Resource):
    pass
#     def post(self):
#         data = request.json
#         database_name = data.get("dataBase")
#         bson_object = db.create_collection(database_name)
#         message = {
#             "message":"user created successfully"
#         }
#         response = json.dumps(message)
#         return response

# class UserRestFullList(Resource):
#     def post(self, id):
#         pass

# api.add_resource(UserRestFull, '/api')
# api.add_resource(UserRestFullList, '/api/<todo_id>')    