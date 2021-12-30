import pytest

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