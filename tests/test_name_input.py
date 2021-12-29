import pytest
from tests.conftest import greet

def test_name_input(client):
    rv = greet(client, 'John')
    
    assert b'John' in rv.data