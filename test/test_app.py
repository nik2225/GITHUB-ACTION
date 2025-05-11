from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_register():
    client = app.test_client()
    response = client.post('/register', data={'name': 'Nikhil', 'email': 'nikhil@example.com'})
    assert response.status_code == 200
    assert b"Registered Nikhil with email nikhil@example.com" in response.data
