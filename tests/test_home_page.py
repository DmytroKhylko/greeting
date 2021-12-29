import pytest

def test_home_page(client):
    '''test if home page loads'''
    rv = client.get('/')
    assert rv.status_code == 200