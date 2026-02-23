from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker 
from dotenv import load_dotenv
import os

load_dotenv()
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST" , "localhost")
DB_NAME = "learning_db"
DB_USER = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False , autoflush=False , bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()





