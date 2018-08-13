import pytest
from app import create_app, db
from app.models import Host


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app('flask_test.cfg')
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def init_database():
    db.create_all()
    host1 = Host(hostname="test-hostname",
                 ll_ip="fe80::932b:9856:dead:beaf/64",
                 ctrl_if="eno1",
                 last_seen="1534186742")

    db.session.add(host1)
    db.session.commit()

    yield db

    db.drop_all()
