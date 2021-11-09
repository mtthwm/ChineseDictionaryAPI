from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    allow_import: bool

    class Config ():
        env_file = '.env'


settings = Settings()