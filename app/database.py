from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_details = {
    "name": "Local database",
    "driver": "PostgreSQL",
    "server": "localhost",
    "port": 5432,
    "database": "postgres",
    "username": "admin",
    "password": "LocalPasswordOnly",
}

SQLALCHEMY_DATABASE_URL = "postgresql://admin:LocalPasswordOnly@localhost/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#  Yes, the code you provided is a database factory. It defines a function get_db() that returns a\
# session object from the SessionLocal class. The session object is used to interact with the database.
# The yield statement allows the function to be used as a generator, providing a context manager-like
# behavior for managing the database session. Finally, the finally block ensures that the session is
# closed properly, even if an exception occurs.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
