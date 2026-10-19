from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://api_postgres_db_tfc2_user:aYakYrZvnZlzzDKIRM3P9k66XhCkWSBr@dpg-dbb66o6i0phs73f3s9v0-a.oregon-postgres.render.com/api_postgres_db_tfc2"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()