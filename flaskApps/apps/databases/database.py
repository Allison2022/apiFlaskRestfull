import json
from flask import Blueprint, request
from flask_restful import Resource
from config import redis_manager, databaseConnection
from apps import api

database = Blueprint('database', __name__)

class EpsDatabase(Resource):
    def post(self):
        data = request.json
        database_name = data.get('database_name')
        collection_name = data.get('collection_name')
        document = data.get('document')
        mongo = databaseConnection(database_name)
        object_mongo = mongo.db[collection_name].insert_one(document)
        return "success"

    def get(self, id=None):
        data = request.json
        return data

class EpsDatabaseList(Resource):
    def put(self, id=None):
        pass

    def delete(self, id=None):
        pass

api.add_resource(EpsDatabase, '/api/database/create', methods=['POST'])
api.add_resource(EpsDatabase, '/api/database/list', '/api/database/detail', endpoint='database', methods=['GET'])
api.add_resource(EpsDatabaseList, '/api/database/update', '/api/database/delete', endpoint='databaseList', methods=['PUT', 'DELETE'])