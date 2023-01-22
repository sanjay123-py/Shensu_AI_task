import pymongo
import os
from logger import logging
from exception import SensorException
import sys
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv()
DATABASE_NAME = "Shen"
COLLECTION_NAME = "ICIC_STOCK"
STOCK_NAME="ICICIBANK.NS"
@dataclass
class Enviroinment:
    mongo_db_url = os.getenv('MONGO_DB_URL')
try:
    env_var = Enviroinment()
    client = pymongo.MongoClient(env_var.mongo_db_url)
except Exception as e:
    raise SensorException(e,sys)
