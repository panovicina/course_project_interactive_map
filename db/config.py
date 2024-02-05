from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config.config import settings

database_url = (f"{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}"
                f":{settings.DB_PORT}/{settings.DB_NAME}")
# engine = create_engine("sqlite:///test.db", echo=True)
engine = create_engine(f'postgresql+psycopg2://{database_url}', echo=True)

session = sessionmaker(engine, expire_on_commit=False)
