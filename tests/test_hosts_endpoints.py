def test_get_hosts(test_client):
    """
    GIVEN a Flash app
    WHEN the '/hosts' page is requested (GET)
    THEN check response is valid
    """
    response = test_client.get('/hosts')
    assert response.status_code == 200