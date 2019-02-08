import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    Testing = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')
