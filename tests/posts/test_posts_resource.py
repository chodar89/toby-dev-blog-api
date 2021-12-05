"""Test Posts resources"""


def test_posts_list_get_200(app, client, db, post):
    res = client.get("/posts/")
    res_json = res.get_json()
    assert res.status_code == 200
    assert len(res_json)
    assert res_json[0]["id"] == str(post.id)


def test_posts_list_post_200(app, client, db):
    res = client.post("/posts/")
    assert res.status_code == 200
