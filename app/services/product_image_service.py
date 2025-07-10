import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.binary import Binary

dotenv_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path)

class ProductImageService:
    def __init__(self):
        mongo_host = os.getenv("MONGO_HOST")
        mongo_port = int(os.getenv("MONGO_PORT"))
        mongo_db = os.getenv("MONGO_DB")
        collection_name = os.getenv("MONGO_COLLECTION")
        
        client = MongoClient(host=mongo_host, port=mongo_port)
        db = client[mongo_db]
        self.collection = db[collection_name]

    def save_image(self, product_id: int, image_data: bytes, filename: str, content_type: str):
        self.collection.delete_many({"product_id": product_id})  # sobrescribe imagen
        self.collection.insert_one({
            "product_id": product_id,
            "image_data": Binary(image_data),
            "filename": filename,
            "content_type": content_type
        })

    def get_image(self, product_id: int):
        return self.collection.find_one({"product_id": product_id})
