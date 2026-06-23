import json

from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session
from shapely.geometry import Point
from shapely.geometry import shape

from app.database import Base
from app.database import engine
from app.database import get_db
from app.model import TblConstituency
from app.schemas import LocationRequest

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="COMS Location Service",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "service": "COMS Location Service",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/check-location")
def check_location(
    request: LocationRequest,
    db: Session = Depends(get_db)
):
    point = Point(request.longitude, request.latitude)

    constituencies = db.query(TblConstituency).all()

    for constituency in constituencies:
        polygon = shape(constituency.geo_json)
        if polygon.contains(point):
            return {
                "inside": True,
                "constituency_id": constituency.id,
                "constituency_name": constituency.constituency_name
            }

    return {
        "inside": False
    }