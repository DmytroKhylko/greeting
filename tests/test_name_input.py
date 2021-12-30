import pytest
from tests.conftest import greet

def test_name_input(client, init_database):
    init_database.session.remove()
    # init_database.drop_all()
    init_database.create_all()
    # response = client.post("/", data=dict(
    #     name = "John"
    # ), follow_redirects=True)

    # assert b'John' in rv.data

    # init_database.session.remove()
    # init_database.drop_all()