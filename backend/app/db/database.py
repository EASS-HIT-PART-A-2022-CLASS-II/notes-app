import motor.motor_asyncio
from core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.DB_HOST, settings.DB_PORT)
database = client[settings.DB_NAME]
collection = database.note
