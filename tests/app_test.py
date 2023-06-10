from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_tc0001_welcome():
    td_message = {'message': 'Hello, welcome to Justice Leagues FastAPI'}

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == td_message


def test_tc0002_health():
    td_message = {"status": "OK"}

    response = client.get('/health')

    assert response.status_code == 200
    assert response.json() == td_message