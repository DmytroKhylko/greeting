import pytest
from tests.conftest import greet

def test_all_greetings(client):
    greet(client, 'John')
    greet(client, 'David')
    rv = client.get('/all-greetings')
    assert b'John' in rv.data
    assert b'David' in rv.data
    assert b'Emely' not in rv.data