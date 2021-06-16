from sqlalchemy.orm import Session

import schemas
import models


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: schemas.PostCreate):
    db_item = models.Post(**post.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
