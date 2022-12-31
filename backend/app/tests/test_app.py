from http import client
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This will be the main window of the Notes APP!!"}

# This app doesn't have a complex logic covered in inner functions.
# The only items which can be tested are the API endpoints.
# All of the API callings ending up by manipulating the DB in some way (CRUD)
# After doing some investigation, it seems that there is no recommended way (or any way) to test these functions with motor
# JIRA for reference: https://jira.mongodb.org/browse/MOTOR-755
# The recommendation is to test the features using a real DB
# Until I find a working solution, the tests will remain as they are and more will be added in the future
