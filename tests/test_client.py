from fastapi.testclient import TestClient
from devins-new-ai.src.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_extract_text_info_endpoint():
    response = client.get("/extract-text/")
    assert response.status_code == 200
    assert "This endpoint accepts POST requests" in response.json()["message"]
