from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel 

from project_afia.database import get_db
from project_afia.models import User

app = FastAPI()


#incoming jason shape
class UserCreate(BaseModel):
    first_name: str
    last_name: str

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.get("/")
async def root():
    return {"message": "Hello World"}



