from pydantic import BaseModel

class LocationRequest(BaseModel):
    latitude: float
    longitude: float