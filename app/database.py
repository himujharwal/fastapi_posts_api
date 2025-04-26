
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql+psycopg2://himu:himu1234@localhost:5432/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# autoflush = false --> SQLAlchemy won’t automatically sync your in-memory changes (Python objects) to the database before a query runs.

Base = declarative_base()

# dependancy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

