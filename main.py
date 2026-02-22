from fastapi import FastAPI , HTTPException , Depends
from database import engine, get_db, Base
from sqlalchemy.orm import Session
import models
import schemas

#Create Table
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/" , response_model=schemas.UserSchema)
def create_user(user: schemas.UserSchema , db: Session=Depends(get_db)):
    existing_user = db.query(models.UserDB).filter(models.UserDB.username == user.username ).first()
    if existing_user:
        raise HTTPException(status_code = 400 , detail = "Username already registered")
    
    new_user = models.UserDB(username = user.username , email=user.email)
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.UserDB).all()


@app.delete("/delete/{user_id}")
def delete_user(user_id: int , db: Session = Depends(get_db)):
    user = db.query(models.UserDB).filter(models.UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404 , detail="User not found")
    
    deleted_id = user.id
    db.delete(user)
    db.commit()
    return{"message":"User deleted " , "User ID" : {deleted_id}}