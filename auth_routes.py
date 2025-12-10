from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import SignUpModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth_router.get('/')
def hello():
    return {"message": "Hello from auth routes!"}

@auth_router.post('/signup',response_model=SignUpModel, status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel, db: Session = Depends(get_db)):
    db_email = db.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    db_username = db.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
