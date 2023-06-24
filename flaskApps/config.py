from apps import app
import secrets
import redis
from flask_pymongo import PyMongo

# -------------------------------------------------------------------------------------------------------
tokens_session = secrets.token_hex(20)
tokens_session = app.config["SECRET_KEY"]

def databaseConnection(database_name):
    try:
        app.config["MONGO_URI"] = f"mongodb+srv://erik1288:ingeniero010@userscluster.vyzqgn5.mongodb.net/{database_name}?retryWrites=true&w=majority"
        print('conection success.......')
        mongo = PyMongo(app)
    except ConnectionError:
        print('conection error...')
    return mongo

# ------------------------------------------------------------------------------------------------------

# redis config
redis_manager = redis.Redis(
  host='redis-10179.c14.us-east-1-3.ec2.cloud.redislabs.com',
  port=10179,
  password='ingeniero010')

# check connection to redis
def checkRedisConnection():
    try:
        response = redis_manager.ping()
        if response:
            print("Connection to Redis successful")
    except redis.ConnectionError:
        print("Failed to connect to Redis")

# Llamar a la función para comprobar la conexión a Redis
checkRedisConnection()
# -------------------------------------------------------------------------------------------------------

class BaseConfig(object):
    'Base configuration'
    TESTING = False
    DEBUG=True
    
class ProductionConfig(BaseConfig):
    'Production configuration'
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    'Development configuration'
    TESTING = True