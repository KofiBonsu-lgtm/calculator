import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import Base  
from app.models.user import User
from app.models.calculations import Base as CalcBase
from app.models.user import Base as UserBase
from app.models.calculations import Calculation
from app.models.user import User

@pytest.fixture(scope="function")
def db_engine():
    engine = create_engine("sqlite:///:memory:", future=True)
    # create all tables (users + calculations)
    UserBase.metadata.create_all(engine)
    CalcBase.metadata.create_all(engine)
    return engine

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db_session():
   
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)
