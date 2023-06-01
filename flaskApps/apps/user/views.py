from flask import Blueprint, request
from flask_restful import Resource
# from apps import redisConnection

user = Blueprint('user', __name__)

class UserRestFull(Resource):
    def post(self):
        data = request.json
        print("holaaaaaa......................")
        print(type(data))
        # response = redisConnection.set()

    # def abort_if_todo_doesnt_exist(self, id):
    #     if todo_id not in TODOS:
    #         abort(404, message="Todo {} doesn't exist".format(todo_id))