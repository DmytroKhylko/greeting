import pytest

from greeting_app.models.db import db
from greeting_app.create_app import create_app
from greeting_app.models.visitor_model import Visitor

@pytest.fixture()
def app():
    app = create_app('greeting_app.config.TestingConfig')
    yield app 
 

@pytest.fixture()
def client(app):
    with app.app_context():
        yield app.test_client()

@pytest.fixture()
def init_database():
    yield db

def greet(client, name):
    return client.post('/', data=dict(
        name=name
    ), follow_redirects=True)
