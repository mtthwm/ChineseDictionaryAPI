from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    run_parser: bool

    class Config ():
        env_file = '.env'


settings = Settings()