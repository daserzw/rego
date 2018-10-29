import pytest
from rego import create_app


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True
    })

    with app.app_context():
        app.db.create_all()
        from rego.models import User
        user = User(name='Test User')
        app.db.session.add(user)
        app.db.session.commit()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
