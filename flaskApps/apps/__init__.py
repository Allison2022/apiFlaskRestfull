import redis
from flask import Flask
from flask_restful import Api
from apps.user.views import UserRestFull

app = Flask(__name__)
api = Api(app)

api.add_resource(UserRestFull, '/useRegistration')

redisConnection = redis.Redis(
  host='redis-10179.c14.us-east-1-3.ec2.cloud.redislabs.com',
  port=10179,
  password='ingeniero010')

from apps.user.views import user

app.register_blueprint(user)