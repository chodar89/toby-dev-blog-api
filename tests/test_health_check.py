"""Check healthcheck endpoint"""


def test_healthcheck(app, client):
    res = client.get("/healthcheck")
    assert res.status_code == 200
