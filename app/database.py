import databases
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

# Define an asynchronous database connection pool using databases
database = databases.Database(DATABASE_URL)

# Create a synchronous SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a declarative base
Base = declarative_base()

# Create a synchronous session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Metadata object to bind SQLAlchemy models to the database
metadata = MetaData()


#  Yes, the code you provided is a database factory. It defines a function get_db() that returns a\
# session object from the SessionLocal class. The session object is used to interact with the database.
# The yield statement allows the function to be used as a generator, providing a context manager-like
# behavior for managing the database session. Finally, the finally block ensures that the session is
# closed properly, even if an exception occurs.


# Function to get an asynchronous database session
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
