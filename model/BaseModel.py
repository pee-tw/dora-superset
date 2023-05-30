from peewee import Model, MySQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")


db = MySQLDatabase(
    DB_NAME, 
    user=DB_USER, 
    password=DB_PASS, 
    host=DB_HOST, 
    port=3306, 
    ssl = {
        "ca": "/etc/ssl/cert.pem"
        }
    )

db.connect()


class BaseModel(Model):
    class Meta:
        database = db
