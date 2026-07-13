from fastapi import APIRouter  , Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import Memory


router = APIRouter()



@router.get("/memories")
def get_memoories(db:Session= Depends(get_db)):

    memories = db.query(Memory).all()
    return memories

@router.get("/")
def root():
    return{
        "status":"sucess"
    }