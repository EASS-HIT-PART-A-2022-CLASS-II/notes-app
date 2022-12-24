from pydantic import BaseModel
from datetime import date
class Note(BaseModel):
    text: str
    date: date

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}