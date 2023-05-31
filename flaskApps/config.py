import secrets
from apps import app

# # secret key for mongo session
# tokenSession = secrets.token_hex(20)

# app.config["SECRET_KEY"]=tokenSession

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