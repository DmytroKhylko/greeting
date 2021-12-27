import pytest

from greeting_app.create_app import create_app

@pytest.fixture()
def app():
    app = create_app('greeting_app.config.TestingConfig')
    yield app 
 

@pytest.fixture()
def client(app):
    with app.app_context():
        yield app.test_client()

def greet(client, name):
    return client.post('/', data=dict(
        name=name
    ), follow_redirects=True)
