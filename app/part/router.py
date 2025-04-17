from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from . import controller, schema

router = APIRouter()

# CRUD OPERATION ENDPOINTS FOR PARTS
@router.get("/", response_model=list[schema.PartResponse])
def list_parts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return controller.get_parts(db, skip=skip, limit=limit)

@router.post("/", response_model=schema.PartResponse, status_code=201)
def post_part(part: schema.PartCreate, db: Session = Depends(get_db)):
    return controller.create_part(db, part)

@router.get("/{part_id}", response_model=schema.PartResponse)
def get_part(part_id: int, db: Session = Depends(get_db)):
    part = controller.get_part(db, part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.put("/{part_id}", response_model=schema.PartResponse)
def update_part(part_id: int, part: schema.PartUpdate, db: Session = Depends(get_db)):
    return controller.update_part(db, part_id, part)

@router.delete("/{part_id}", response_model=schema.PartResponse)
def delete_part(part_id: int, db: Session = Depends(get_db)):
    return controller.delete_part(db, part_id)

# DESCRIPTION STATS ENDPOINTS
@router.get("/description-stats/")
def description_stats(db: Session = Depends(get_db)):
    return {"top_words": controller.get_top_words(db)}
