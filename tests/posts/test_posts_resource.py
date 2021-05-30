"""Test Posts resources"""


def test_posts_list_get_200(app, client, db):
    res = client.get("/posts/")
    assert res.status_code == 200


def test_posts_list_post_200(app, client, db):
    res = client.post("/posts/")
    assert res.status_code == 200
