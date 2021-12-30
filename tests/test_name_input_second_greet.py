import pytest
from tests.conftest import greet

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