from pydantic import BaseModel

class SensorData(BaseModel):
    name: str
    location: str
    spo2: float
    alt_sensor: float
    temp: float
