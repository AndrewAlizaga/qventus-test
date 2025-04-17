from fastapi import FastAPI
from app.part import model
from app.part.router import router as part_router
from app.db import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(part_router, prefix="/parts", tags=["parts"])
