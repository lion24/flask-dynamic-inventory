import pytest
from app import create_app
from app.database import db as _db


@pytest.fixture(scope="module")
def app():
    app = create_app('flask_test.cfg', testing=True)

    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.fixture(scope="module")
def test_client(app):
    yield app.test_client()


@pytest.fixture(scope='function')
def db(app):
    _db.app = app
    _db.create_all()

    yield _db

    _db.drop_all()


@pytest.fixture(scope='function')
def session(db):
    connection = _db.engine.connect()
    transaction = connection.begin()

    session = _db.create_scoped_session()

    _db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
