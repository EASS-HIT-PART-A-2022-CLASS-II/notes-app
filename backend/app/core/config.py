import os

class Settings:
    PROJECT_NAME: str = 'Notes APP'
    PROJECT_VERSION: str = '1.0.0'
    DB_NAME: str = os.getenv("db")
    DB_HOST: str = 'mongodb://notes-app-DB'
    DB_PORT: int = int(os.getenv('db_port'))
    DB_PATH: '{host}:{port}'.format(host=DB_HOST, port=DB_PORT)

settings = Settings()