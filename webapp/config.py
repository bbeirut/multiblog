from os import path

class Config(object):
    SECRET_KEY = 'ee27ead3f4c0fc52f699379882775d33'
    RECAPTCHA_PUBLIC_KEY = '6LdsXBMUAAAAABy3ELvsji6ZKzQbW4MCVdMzFPSD'
    RECAPTCHA_PRIVATE_KEY = '6LdsXBMUAAAAAM9UpnYcfG37XNlX1eEaHltYEeXn'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(
        path.pardir,
        'blog.db'
    )