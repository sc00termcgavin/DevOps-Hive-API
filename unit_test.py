from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app=app)

# version unit test to check the JSON response
def test_version():
    response = client.get('/version')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"version": "v0.0.1"} 

def test_temp():
    response = client.get('/temperature')
    assert response.status_code == status.HTTP_200_OK