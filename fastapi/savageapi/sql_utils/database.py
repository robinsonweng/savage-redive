from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "postgres"
passwd = "example"
SQLALCHEMY_DATABSE_URL = f"postgresql://{user}:{passwd}@savage-psql:5432/dev_anime"

engine = create_engine(
    SQLALCHEMY_DATABSE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
