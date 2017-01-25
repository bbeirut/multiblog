from os import path

class Config(object):
    SECRET_KEY = 'ee27ead3f4c0fc52f699379882775d33'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(
        path.pardir,
        'blog.db'
    )