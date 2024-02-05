import os

from dotenv import find_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str


    class Config:
        env_file = find_dotenv('.env')
        env_file_encoding = "utf-8"


settings = Settings()