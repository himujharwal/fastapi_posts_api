from fastapi import FastAPI, Response, status, HTTPException,Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, utils, oauth2
from app.database import get_db

router = APIRouter(
    prefix="/posts",                                # so the "/" is replace by "/posts"  for every route
    tags=['posts']              #  this will group the fastapi swagger ui into users and posts        
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
    # new_post =  models.Post(title=post.title, content=post.content, published=post.published)
    print("====================",current_user.id)
    new_post = models.Post(owner_id = current_user.id, **post.dict())  # this does same thing like above line but automatically 
    # new_post = models.Post(**post.model_dump())  # this is new way for pydantic v2 
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  #  this will retrive the post that added by comit() in new_post object
    return new_post


@router.get("/", response_model=List[schemas.Post])  # WE have to specify the list here becuase it is returning a list but our schema we only define a single object so we use the List from typing library
def get_all(db:Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    return posts


@router.get("/{id}", response_model=schemas.Post)
def get_post(id:int, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return post



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if post.owner_id !=  current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="could not authorises credetnaital")
    
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int, updated_post: schemas.PostCreate ,db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()



    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if post.owowner_id !=  current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="could not authorises credetnaital")
    
    # post_query.update({'title':"this is my updatealbe title", 'content':"my contetne"})
    post_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()
