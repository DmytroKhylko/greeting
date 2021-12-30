import pytest
from tests.conftest import greet

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_name_input_blank(client, init_database):
    init_database.drop_all()
    init_database.create_all()

    response = client.post("/", data=dict(
        name = ""
    ), follow_redirects=True)

    assert bytes("Поле не може бути пустим", 'utf-8') in response.data

    init_database.session.remove()
    init_database.drop_all()

def test_name_input_first_greet(client, init_database):
    init_database.drop_all()
    init_database.create_all()

    response = client.post("/", data=dict(
        name = "John"
    ), follow_redirects=True)

    assert bytes("Привіт, John", 'utf-8') in response.data

    init_database.session.remove()
    init_database.drop_all()

def test_name_input_second_greet(client, init_database):
    init_database.drop_all()
    init_database.create_all()

    greet(client, "John")

    response = client.post("/", data=dict(
        name = "John"
    ), follow_redirects=True)

    assert bytes("Вже бачились, John", 'utf-8') in response.data

    init_database.session.remove()
    init_database.drop_all()
