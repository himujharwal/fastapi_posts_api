from fastapi import FastAPI, Response, status, HTTPException,Depends
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, utils
from app.database import engine, get_db

from app.routers import post, user, auth





models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)




@app.get("/")
def home():
    return "Welcome to FastAPI learning page"







