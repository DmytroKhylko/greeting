import pytest
from tests.conftest import greet

def test_home_page(client):
    '''test if home page loads'''
    rv = client.get('/')
    assert rv.status_code == 200

def test_name_input_blank(client, init_database):
    """
    GIVEN visitor
    WHEN visitor sumbmits empty name
    THEN check if warning is shown "Поле не може бути пустим"
    """
    init_database.drop_all()
    init_database.create_all()
    response = client.post("/", data=dict(
        name = ""
    ), follow_redirects=True)

    assert b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xb5 \xd0\xbd\xd0\xb5 \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xb5 \xd0\xb1\xd1\x83\xd1\x82\xd0\xb8 \xd0\xbf\xd1\x83\xd1\x81\xd1\x82\xd0\xb8\xd0\xbc' in response.data

    init_database.session.remove()
    init_database.drop_all()

def test_name_input_first_greet(client, init_database):
    """
    GIVEN visitor
    WHEN visitor types one's name
    THEN check if return message is: Привіт, <visitor_name>
    """
    init_database.drop_all()
    init_database.create_all()
    response = client.post("/", data=dict(
        name = "John"
    ), follow_redirects=True)

    assert b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82, John' in response.data

    init_database.session.remove()
    init_database.drop_all()

def test_name_input_second_greet(client, init_database):
    """
    GIVEN visitor
    WHEN visitor types one's name
    THEN check if return message is: Вже бачились, <visitor_name>
    """
    init_database.drop_all()
    init_database.create_all()

    greet(client, "John")

    response = client.post("/", data=dict(
        name = "John"
    ), follow_redirects=True)

    assert b'\xd0\x92\xd0\xb6\xd0\xb5 \xd0\xb1\xd0\xb0\xd1\x87\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x81\xd1\x8c, John' in response.data

    init_database.session.remove()
    init_database.drop_all()
