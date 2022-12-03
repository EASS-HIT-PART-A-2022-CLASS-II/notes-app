import os

class Settings:
    PROJECT_NAME: str = 'Notes APP'
    PROJECT_VERSION: str = '1.0.0'
    DEFAULT_DB_NAME: str = 'Test'
    DB_NAME: str = os.getenv("db", DEFAULT_DB_NAME)
    DB_HOST: str = 'mongodb://notes-app-DB'
    DEFAULT_PORT: int = 27017
    DB_PORT: int = int(os.getenv('db_port', DEFAULT_PORT))

settings = Settings()