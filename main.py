from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import schemas
import models
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/posts/", response_model=schemas.Post)
def create_post(
        post: schemas.PostCreate, db: Session = Depends(get_db)
):
    return crud.create_post(db=db, post=post)


@app.get("/list/", response_model=List[schemas.Post])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts
