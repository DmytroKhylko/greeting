import pytest

def test_name_input_first_greet(client, init_database):
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