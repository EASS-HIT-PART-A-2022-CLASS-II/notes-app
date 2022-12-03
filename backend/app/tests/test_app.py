from http import client
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This will be the main window of the Notes APP!!"}

# TODO: learn how to mock mongodb for testing the other endpoints