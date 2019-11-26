import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    APP_NAME = os.getenv('APP_NAME', 'Blog')
    FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', '8000')
    FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    DEBUG = os.getenv('DEBUG', False)
    DATABASE = {
        'name': 'test.db',
        'engine': 'peewee.SqliteDatabase',
    }
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    CREATE_ADMIN = os.getenv('CREATE_ADMIN', False)
    SECRET_KEY = 'SO_SECRET'
    SESSION_TYPE = 'filesystem'
