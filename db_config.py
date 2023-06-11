from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# resource: https://fastapi.tiangolo.com/tutorial/sql-databases/

SQLALCHEMY_DATABASE_URL = "sqlite:///./db/database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


# starting point for sqlalchemy
engine = create_engine(
    # only needed for sqlite db
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# each instance of SessionLocal is a db instance.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


# Dependency 
def get_db():
    db = SessionLocal()
    try: 
        # yield returns the object instead of the value
        yield db
    finally:
        db.close()