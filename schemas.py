from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str

    # This configuration tells Pydantic: "It's okay to read data from ORM objects"
    class Config:
        from_attributes = True
        