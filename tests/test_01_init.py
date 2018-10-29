import pytest
import flask
from rego import create_app, page_not_found, internal_server_error

#def test_load_user(app):
#    assert app.load_user(0) == 1

def test_create_app():
    test_app = create_app()
    assert isinstance(test_app, flask.Flask)

def test_index(client):
    response = client.get('/')
    assert b'Hello' in response.data

def test_404(client):
    response = client.get('/not_found')
    assert response.status_code == 404
    
def test_page_not_found(app):
    with app.app_context():
        assert page_not_found('error')[1] == 404
    
def test_internal_server_error(app):
    with app.app_context():
        assert internal_server_error('error')[1] == 500
    
