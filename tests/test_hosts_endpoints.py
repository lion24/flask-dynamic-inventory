import json
import sys


def test_home_api(test_client):
    """
    GIVEN a Flask app
    WHEN one of ('/', '/home', '/index') pages is requested (GET)
    THEN check response is valid
    """
    reqs = ('/', '/home', '/index')
    for req in reqs:
        response = test_client.get(req)
        assert response.status_code == 200
        assert json.loads(response
                          .get_data()
                          .decode(sys
                                  .getdefaultencoding())) == {'hello': 'world'}


def test_get_hosts(test_client, db):
    """
    GIVEN a Flask app
    WHEN the '/hosts' page is requested (GET)
    THEN check response contains valid datas
    """
    response = test_client.get('/hosts')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert int(response.headers['Content-Length']) > 0

    # dummy = {}
    # dummy.update(hostname="test-hostname",
    #              ll_ip="fe80::932b:9856:dead:beaf/64",
    #              ctrl_if="eno1",
    #              last_seen=datetime.now())
    # hosts = json.loads(response.get_data().decode(sys.getdefaultencoding()))
