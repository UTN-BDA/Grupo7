import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.binary import Binary

dotenv_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path)

class ProductImageService:
    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI")
        collection_name = os.getenv("MONGO_COLLECTION")
        
        client = MongoClient(mongo_uri)
        db_name = mongo_uri.split("/")[-1].split("?")[0]
        db = client[db_name]
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

    def delete_image(self, product_id):
        result = self.collection.delete_one({"product_id": product_id})
        return result.deleted_count > 0