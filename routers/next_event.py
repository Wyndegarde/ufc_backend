from fastapi import APIRouter, Depends

from database import SessionLocal
from models import NextEventTruncated

ne_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@ne_router.get("/next_event")
async def get_next_event(db=Depends(get_db)):
    return db.query(NextEventTruncated).all()
