from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data = {
        "firstName": "Fa", 
        "lastName": "BA", 
        "email": "fa.ba@gmail.com", 
        "password": "qwerzccb.", 
        "gender": "male", 
    }

def test_get_all_admins():
    response = client.get('/api/admins',json = data)
    assert response.status_code == 200
    assert response.json()

def test_get_admin_by_id():
    response = client.get('/api/admins',json = data)
    response = client.get("/api/admins/1/")
    assert response.status_code == 200
    assert response.json()["email"] == "fa.ba@gmail.com"

def test_create_admin():
    response = client.post('/api/admins', json=data)
    assert response.status_code == 200
    assert response.json()["email"] == "fa.ba@gmail.com"
    assert response.json()["firstName"] == "Fa"
