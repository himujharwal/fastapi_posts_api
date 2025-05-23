
from fastapi import FastAPI, Response, status, HTTPException,Depends, APIRouter
from sqlalchemy.orm import Session
from app import models, schemas, utils, oauth2
from app import  database


router = APIRouter(
    prefix="/users",
    tags=['users']
)

@router.post("/", status_code=status.HTTP_201_CREATED , response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate , db: Session = Depends(database.get_db),current_user:int = Depends(oauth2.get_current_user)):


    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())  
    # new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 
    return new_user




@router.get("/{id}", response_model=schemas.UserOut)
def get_post(id:int, db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"user id {id} does not exist"})
    
    return user
