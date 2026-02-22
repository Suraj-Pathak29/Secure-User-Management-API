from database import Base
from sqlalchemy import Column , String , Integer  

class UserDB(Base):
    __tablename__ = 'api_users'
    id  = Column(Integer, primary_key=True , index=True)
    username = Column(String(50), unique=True , index=True)
    email = Column(String)