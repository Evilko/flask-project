import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    APP_NAME = os.getenv('APP_NAME', 'Blog')
    FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', '8000')
    FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST', '8000')
    DEBUG = os.getenv('DEBUG', False)
