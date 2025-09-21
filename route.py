from fastapi import APIRouter
from models import SensorData
from database import db
import uuid

router = APIRouter()

@router.post("/api/app/data/{id}")
async def post_app_data(id: int):
    return {"message": f"Received POST for app data with id: {id}"}

@router.get("/api/app/data/{id}")
async def get_app_data(id: int):
    return {"message": f"Received GET for app data with id: {id}"}

@router.get("/api/website/data")
async def get_website_data():
    return {"message": "Received GET for website data"}

@router.get("/api/website/data/{id}")
async def get_website_data_by_id(id: int):
    return {"message": f"Received GET for website data with id: {id}"}

@router.post("/sensor-data")
async def store_sensor_data(data: SensorData):
    collection = db.get_collection("sensor_data")
    
    document = data.dict()
    document["unique_id"] = str(uuid.uuid4())

    result = collection.insert_one(document)
    
    return {"message": "Data stored successfully", "inserted_id": str(result.inserted_id), "unique_id": document["unique_id"]}

@router.get("/sensor-data")
async def get_all_sensor_data():
    collection = db.get_collection("sensor_data")
    
    # Get all documents from the collection
    cursor = collection.find({})
    data = []
    
    for document in cursor:
        # Convert ObjectId to string for JSON serialization
        document["_id"] = str(document["_id"])
        data.append(document)
    
    print(f"Found {len(data)} documents")

    return {"data": data, "count": len(data)}

@router.get("/sensor-data/{unique_id}")
async def get_sensor_data_by_id(unique_id: str):
    collection = db.get_collection("sensor_data")
    
    # Find document by unique_id
    document = collection.find_one({"unique_id": unique_id})
    
    if document:
        # Convert ObjectId to string for JSON serialization
        document["_id"] = str(document["_id"])
        return {"data": document}
    else:
        return {"message": "Data not found", "unique_id": unique_id}