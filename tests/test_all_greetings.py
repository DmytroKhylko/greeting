import pytest
from tests.conftest import greet

def test_all_greetings(client, init_database):
    """
    GIVEN visitor
    WHEN visitor John and visitor David greeted
    THEN check if John and David are in list of greeted visitors
    """
    init_database.drop_all()
    init_database.create_all()
    greet(client, "John")
    greet(client, "David")
    response = client.get('/all-greetings')
    assert b'John' in response.data
    assert b'David' in response.data

    init_database.session.remove()
    init_database.drop_all()