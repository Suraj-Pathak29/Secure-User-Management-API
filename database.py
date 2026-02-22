from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker 
from dotenv import load_dotenv
import os

load_dotenv()
DB_PASS = os.getenv("DB_PASSWORD")
DATABASE_URL = f"postgresql://postgres:{DB_PASS}@localhost/learning_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False , autoflush=False , bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()





