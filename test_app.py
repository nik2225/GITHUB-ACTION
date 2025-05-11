# test_app.py
from flask import Flask

def test_home():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'Hello, world!'
    
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
