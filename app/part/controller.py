from sqlalchemy.orm import Session
from . import model, schema
from collections import Counter
import re

def get_part(db: Session, part_id: int):
    """Fetch a part by its ID."""
    return db.query(model.Part).filter(model.Part.id == part_id).first()

def get_parts(db: Session, skip: int = 0, limit: int = 10):
    """Fetch parts with pagination."""
    return db.query(model.Part).offset(skip).limit(limit).all()

def create_part(db: Session, part: schema.PartCreate):
    """Create a new part."""
    db_part = model.Part(**part.dict())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

def update_part(db: Session, part_id: int, updated: schema.PartUpdate):
    """Update an existing part by id."""
    db_part = get_part(db, part_id)
    if db_part:
        for key, value in updated.dict().items():
            setattr(db_part, key, value)
        db.commit()
        db.refresh(db_part)
    return db_part

def delete_part(db: Session, part_id: int):
    """Delete a part by id."""
    db_part = get_part(db, part_id)
    if db_part:
        db.delete(db_part)
        db.commit()
    return db_part

def get_top_words(db: Session, n=5):
    """Get the top N most common words from part descriptions."""
    parts = db.query(model.Part).all()
    text = " ".join(p.description for p in parts)
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words).most_common(n)
