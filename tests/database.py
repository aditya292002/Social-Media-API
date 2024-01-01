import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from app import models

import databases
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from app.config import settings

DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test"

# Define an asynchronous database connection pool using databases
database = databases.Database(DATABASE_URL)

# Create a synchronous SQLAlchemy engine
engine = create_engine(DATABASE_URL)


# Create a synchronous session factory
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Metadata object to bind SQLAlchemy models to the database
metadata = MetaData()


#  Yes, the code you provided is a database factory. It defines a function get_db() that returns a\
# session object from the SessionLocal class. The session object is used to interact with the database.
# The yield statement allows the function to be used as a generator, providing a context manager-like
# behavior for managing the database session. Finally, the finally block ensures that the session is
# closed properly, even if an exception occurs.


# @pytest.fixture(scope="module")
# def session():
#     models.Base.metadata.drop_all(bind=engine)
#     models.Base.metadata.create_all(bind=engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @pytest.fixture(scope="module")
# def client(session):
#     # Function to get an asynchronous database session
#     async def override_get_db():
#         try:
#             yield session
#         finally:
#             session.close()

#     app.dependency_overrides[get_db] = override_get_db
#     yield TestClient(app)


@pytest.fixture()
def session():
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    # Function to get an asynchronous database session
    async def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
