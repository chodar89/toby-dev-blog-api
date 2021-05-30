"""Test Posts resources"""
from tests.factories import PostFactory


def test_posts_list_get_200(app, client, db):
    res = client.get("/posts/")
    res_json = res.get_json()
    assert res.status_code == 200


def test_posts_list_post_200(app, client, db):
    res = client.post("/posts/")
    assert res.status_code == 200
